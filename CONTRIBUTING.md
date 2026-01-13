# Contributing to IdeaForge

Thank you for your interest in contributing to IdeaForge! This document provides guidelines for contributing to the project.

## 🎯 Project Philosophy

IdeaForge is a **personal framework** for evaluating and developing passive income ideas using machine learning. While it's primarily for personal use, contributions that improve the framework are welcome.

## 🤝 How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. **Check existing issues** to avoid duplicates
2. **Open a new issue** with:
   - Clear, descriptive title
   - Detailed description of the problem/suggestion
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)

### Suggesting Enhancements

We welcome ideas for:
- New evaluation criteria
- Improved ML scoring algorithms
- Additional idea templates
- Better documentation
- Automation scripts
- Performance improvements

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/heybearc/IdeaForge.git
   cd IdeaForge
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation as needed

4. **Test your changes**
   ```bash
   # Run the ML scorer
   python ml-engine/idea-scorer/evaluate.py ideas/brainstorm/test-idea.md
   
   # Verify no errors
   ```

5. **Commit with clear messages**
   ```bash
   git commit -m "Add: New evaluation criteria for market timing"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Describe what you changed and why
   - Reference any related issues
   - Explain how to test your changes

## 📋 Contribution Guidelines

### Code Style

- **Python**: Follow PEP 8 style guide
- **Markdown**: Use consistent formatting
- **Comments**: Explain WHY, not WHAT
- **Naming**: Use descriptive variable/function names

### Commit Messages

Use conventional commit format:
- `Add:` New features or files
- `Fix:` Bug fixes
- `Update:` Changes to existing features
- `Docs:` Documentation updates
- `Refactor:` Code restructuring
- `Test:` Adding or updating tests

Examples:
```
Add: New ML criterion for competitive analysis
Fix: Scoring calculation for automation level
Update: Evaluation matrix with clearer descriptions
Docs: Add examples to QUICKSTART guide
```

### Documentation

- Update README.md if you add new features
- Add comments to complex code
- Update QUICKSTART.md for workflow changes
- Create examples for new templates

## 🧪 Testing

Before submitting a PR:

1. **Test ML evaluation**
   ```bash
   python ml-engine/idea-scorer/evaluate.py ideas/brainstorm/test-idea.md
   ```

2. **Verify templates work**
   ```bash
   cp frameworks/idea-template.md ideas/brainstorm/test.md
   # Fill in test data and evaluate
   ```

3. **Check documentation**
   - All links work
   - Code examples are correct
   - Instructions are clear

## 🎨 Areas for Contribution

### High Priority
- [ ] Improved ML scoring algorithm
- [ ] Automated performance tracking
- [ ] Integration with project management tools
- [ ] Better visualization of idea scores
- [ ] API for programmatic access

### Medium Priority
- [ ] Additional idea templates (SaaS, content, etc.)
- [ ] Market research automation
- [ ] Competitor analysis tools
- [ ] Success pattern recognition
- [ ] Export to various formats

### Low Priority
- [ ] Web interface for idea management
- [ ] Mobile app for idea capture
- [ ] Integration with note-taking apps
- [ ] Social sharing features
- [ ] Community idea marketplace

## 🚫 What We Don't Accept

- Changes that make the framework more complex without clear benefit
- Features that require external services (keep it self-contained)
- Opinionated business advice (framework should be neutral)
- Breaking changes without migration path
- Undocumented features

## 📝 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 💬 Questions?

- Open an issue for discussion
- Tag with `question` label
- Be specific about what you need help with

## 🙏 Thank You!

Every contribution helps make IdeaForge better. Whether it's:
- Fixing a typo
- Improving documentation
- Adding a feature
- Reporting a bug
- Suggesting an enhancement

**Your contribution matters!**

---

**Remember**: The goal is to help people build passive income systematically. Keep that focus in mind with every contribution.
