# Security Policy

## Purpose

This framework is **defensive security research** designed to improve AI safety. It generates adversarial test prompts to evaluate whether LLMs properly refuse requests that could facilitate human trafficking and labor exploitation.

**Success = Model REFUSES harmful requests.**

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 4.x     | :white_check_mark: |
| 3.x     | :white_check_mark: |
| < 3.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in this framework, please report it responsibly:

1. **Do NOT open a public GitHub issue** for security vulnerabilities.
2. Email the maintainer at the address listed in the repository.
3. Include a description of the vulnerability, steps to reproduce, and potential impact.
4. You will receive an acknowledgment within 48 hours.

## Scope

### In Scope

- Vulnerabilities in the web dashboard (XSS, CSRF, injection)
- API authentication bypass or privilege escalation
- Information disclosure through API responses
- Dependency vulnerabilities in production dependencies
- Unsafe deserialization or code execution in data processing

### Out of Scope

- The adversarial test prompts themselves (these are the intended output)
- Generated training scripts (these are templates, not executed by the framework)
- Issues in development-only dependencies
- Social engineering of the project maintainers

## Ethical Use

This framework is intended for:

- AI safety research and red-teaming
- Improving LLM refusal capabilities for exploitation-related content
- Academic research on adversarial robustness
- Training data generation for safety alignment

It is **NOT** intended for:

- Generating actual exploitation playbooks
- Circumventing safety measures in production systems
- Creating tools for human trafficking or labor exploitation

## Responsible Disclosure

We follow a 90-day responsible disclosure policy. After reporting, we will:

1. Acknowledge receipt within 48 hours
2. Provide an initial assessment within 7 days
3. Work on a fix and coordinate disclosure
4. Credit the reporter in the CHANGELOG (unless anonymity is preferred)
