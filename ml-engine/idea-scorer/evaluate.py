#!/usr/bin/env python3
"""
ML-Powered Idea Evaluation System

Scores passive income ideas based on multiple criteria and learns from outcomes.
"""

import json
import os
from datetime import datetime
from pathlib import Path
import re

class IdeaScorer:
    def __init__(self, lab_root="/Users/cory/Documents/Cloudy-Work/passive-income-lab"):
        self.lab_root = Path(lab_root)
        self.models_dir = self.lab_root / "ml-engine" / "models"
        self.models_dir.mkdir(parents=True, exist_ok=True)
        self.training_data_file = self.models_dir / "training_data.json"
        self.load_training_data()
    
    def load_training_data(self):
        """Load historical idea outcomes for ML training"""
        if self.training_data_file.exists():
            with open(self.training_data_file, 'r') as f:
                self.training_data = json.load(f)
        else:
            self.training_data = []
    
    def save_training_data(self):
        """Save training data for future ML model training"""
        with open(self.training_data_file, 'w') as f:
            json.dump(self.training_data, f, indent=2)
    
    def extract_scores_from_markdown(self, md_file):
        """Extract evaluation scores from markdown idea file"""
        with open(md_file, 'r') as f:
            content = f.read()
        
        scores = {}
        
        # Extract individual scores
        patterns = {
            'market_demand': r'Market Demand:\s*(\d+)\s*/\s*10',
            'technical_feasibility': r'Technical Feasibility:\s*(\d+)\s*/\s*10',
            'time_to_revenue': r'Time to Revenue:\s*(\d+)\s*/\s*10',
            'scalability': r'Scalability:\s*(\d+)\s*/\s*10',
            'initial_investment': r'Initial Investment:\s*(\d+)\s*/\s*10',
            'competitive_advantage': r'Competitive Advantage:\s*(\d+)\s*/\s*10',
            'automation_potential': r'Automation Potential:\s*(\d+)\s*/\s*10',
            'recurring_revenue': r'Recurring Revenue:\s*(\d+)\s*/\s*10',
        }
        
        for key, pattern in patterns.items():
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                scores[key] = int(match.group(1))
            else:
                scores[key] = 0
        
        # Extract metadata
        metadata = {}
        
        # Extract category
        category_match = re.search(r'\*\*Category:\*\*\s*\[(.*?)\]', content)
        if category_match:
            metadata['category'] = category_match.group(1).split('|')[0].strip()
        
        # Extract date
        date_match = re.search(r'\*\*Date Created:\*\*\s*(\d{4}-\d{2}-\d{2})', content)
        if date_match:
            metadata['date_created'] = date_match.group(1)
        
        return scores, metadata
    
    def calculate_weighted_score(self, scores):
        """Calculate weighted total score"""
        weights = {
            'market_demand': 0.15,
            'technical_feasibility': 0.10,
            'time_to_revenue': 0.15,
            'scalability': 0.20,
            'initial_investment': 0.10,
            'competitive_advantage': 0.15,
            'automation_potential': 0.10,
            'recurring_revenue': 0.05,
        }
        
        total = sum(scores.get(key, 0) * weight * 10 for key, weight in weights.items())
        return round(total, 1)
    
    def get_recommendation(self, score):
        """Get action recommendation based on score"""
        if score >= 80:
            return {
                'action': 'Build MVP',
                'priority': 'HIGH',
                'timeline': 'Start this month',
                'next_steps': [
                    'Define MVP feature set',
                    'Set up development environment',
                    'Build core functionality',
                    'Beta test with 10 users'
                ]
            }
        elif score >= 60:
            return {
                'action': 'Validate Market',
                'priority': 'MEDIUM',
                'timeline': 'Validate this week',
                'next_steps': [
                    'Interview 20 potential customers',
                    'Research 5 competitors',
                    'Create landing page',
                    'Collect 50+ email signups'
                ]
            }
        elif score >= 40:
            return {
                'action': 'Refine Idea',
                'priority': 'LOW',
                'timeline': 'Re-evaluate in 2 weeks',
                'next_steps': [
                    'Identify core weakness',
                    'Brainstorm 3 variations',
                    'Re-score best variation',
                    'Archive if still <60'
                ]
            }
        else:
            return {
                'action': 'Archive',
                'priority': 'NONE',
                'timeline': 'Document lessons learned',
                'next_steps': [
                    'Extract key insights',
                    'Update ML training data',
                    'Move to archived folder',
                    'Focus on higher-scoring ideas'
                ]
            }
    
    def analyze_strengths_weaknesses(self, scores):
        """Identify top strengths and weaknesses"""
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        strengths = []
        weaknesses = []
        
        for key, value in sorted_scores[:3]:
            if value >= 7:
                strengths.append(f"{key.replace('_', ' ').title()}: {value}/10")
        
        for key, value in sorted_scores[-3:]:
            if value <= 5:
                weaknesses.append(f"{key.replace('_', ' ').title()}: {value}/10")
        
        return strengths, weaknesses
    
    def predict_success_probability(self, scores, metadata):
        """
        ML prediction of success probability
        Currently uses rule-based heuristics; will evolve to trained model
        """
        total_score = self.calculate_weighted_score(scores)
        
        # Base probability from score
        base_prob = total_score / 100
        
        # Adjust based on category expertise
        category_multipliers = {
            'trading-bots': 1.2,  # High expertise
            'infrastructure-tools': 1.15,  # High expertise
            'api-services': 1.1,  # Good expertise
            'automation-services': 1.05,  # Good expertise
            'content-monetization': 0.9,  # Less experience
        }
        
        category = metadata.get('category', '')
        multiplier = category_multipliers.get(category, 1.0)
        
        # Adjust based on key factors
        if scores.get('scalability', 0) >= 8 and scores.get('automation_potential', 0) >= 8:
            multiplier *= 1.1  # Highly scalable and automated = better for passive income
        
        if scores.get('time_to_revenue', 0) >= 7:
            multiplier *= 1.05  # Fast revenue = lower risk
        
        final_prob = min(base_prob * multiplier, 0.95)  # Cap at 95%
        
        return round(final_prob * 100, 1)
    
    def evaluate_idea(self, md_file):
        """Main evaluation function"""
        md_path = Path(md_file)
        
        if not md_path.exists():
            print(f"❌ Error: File not found: {md_file}")
            return
        
        print(f"\n{'='*60}")
        print(f"📊 EVALUATING IDEA: {md_path.stem}")
        print(f"{'='*60}\n")
        
        # Extract scores
        scores, metadata = self.extract_scores_from_markdown(md_path)
        
        # Calculate total score
        total_score = self.calculate_weighted_score(scores)
        
        # Get recommendation
        recommendation = self.get_recommendation(total_score)
        
        # Analyze strengths/weaknesses
        strengths, weaknesses = self.analyze_strengths_weaknesses(scores)
        
        # Predict success probability
        success_prob = self.predict_success_probability(scores, metadata)
        
        # Display results
        print(f"📈 TOTAL SCORE: {total_score}/100")
        print(f"🎯 SUCCESS PROBABILITY: {success_prob}%")
        print(f"\n🎬 RECOMMENDATION: {recommendation['action']}")
        print(f"⚡ PRIORITY: {recommendation['priority']}")
        print(f"⏰ TIMELINE: {recommendation['timeline']}")
        
        if strengths:
            print(f"\n✅ TOP STRENGTHS:")
            for strength in strengths:
                print(f"   • {strength}")
        
        if weaknesses:
            print(f"\n⚠️  AREAS TO IMPROVE:")
            for weakness in weaknesses:
                print(f"   • {weakness}")
        
        print(f"\n📋 NEXT STEPS:")
        for i, step in enumerate(recommendation['next_steps'], 1):
            print(f"   {i}. {step}")
        
        # Save to training data
        training_entry = {
            'idea_id': md_path.stem,
            'date_evaluated': datetime.now().isoformat(),
            'category': metadata.get('category', 'unknown'),
            'scores': scores,
            'total_score': total_score,
            'success_probability': success_prob,
            'recommendation': recommendation['action'],
            'outcome': 'pending',  # Will be updated later
            'actual_revenue_30d': 0,
            'actual_revenue_90d': 0,
            'actual_revenue_1y': 0,
        }
        
        self.training_data.append(training_entry)
        self.save_training_data()
        
        print(f"\n💾 Evaluation saved to ML training data")
        print(f"{'='*60}\n")
        
        return {
            'total_score': total_score,
            'success_probability': success_prob,
            'recommendation': recommendation,
            'strengths': strengths,
            'weaknesses': weaknesses,
        }
    
    def rank_all_ideas(self, ideas_dir=None):
        """Rank all ideas in a directory"""
        if ideas_dir is None:
            ideas_dir = self.lab_root / "ideas" / "evaluated"
        
        ideas_dir = Path(ideas_dir)
        
        if not ideas_dir.exists():
            print(f"❌ Directory not found: {ideas_dir}")
            return
        
        idea_files = list(ideas_dir.glob("*.md"))
        
        if not idea_files:
            print(f"No ideas found in {ideas_dir}")
            return
        
        print(f"\n{'='*60}")
        print(f"🏆 RANKING ALL IDEAS")
        print(f"{'='*60}\n")
        
        rankings = []
        
        for idea_file in idea_files:
            scores, metadata = self.extract_scores_from_markdown(idea_file)
            total_score = self.calculate_weighted_score(scores)
            success_prob = self.predict_success_probability(scores, metadata)
            
            rankings.append({
                'name': idea_file.stem,
                'score': total_score,
                'probability': success_prob,
                'category': metadata.get('category', 'unknown'),
            })
        
        # Sort by success probability
        rankings.sort(key=lambda x: x['probability'], reverse=True)
        
        print(f"{'Rank':<6} {'Idea':<40} {'Score':<10} {'Probability':<12} {'Category'}")
        print(f"{'-'*6} {'-'*40} {'-'*10} {'-'*12} {'-'*20}")
        
        for i, idea in enumerate(rankings, 1):
            print(f"{i:<6} {idea['name'][:40]:<40} {idea['score']:<10.1f} {idea['probability']:<12.1f}% {idea['category']}")
        
        print(f"\n{'='*60}\n")
        
        return rankings


if __name__ == "__main__":
    import sys
    
    scorer = IdeaScorer()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "rank":
            # Rank all ideas
            if len(sys.argv) > 2:
                scorer.rank_all_ideas(sys.argv[2])
            else:
                scorer.rank_all_ideas()
        else:
            # Evaluate specific idea
            scorer.evaluate_idea(sys.argv[1])
    else:
        print("Usage:")
        print("  python evaluate.py <idea-file.md>     # Evaluate single idea")
        print("  python evaluate.py rank [directory]   # Rank all ideas")
