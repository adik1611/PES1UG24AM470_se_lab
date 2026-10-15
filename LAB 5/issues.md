
# Lab 5 — Static Code Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe eval usage | Security — Medium | 42 | eval() evaluates a supplied expression and may execute unintended code. | Replaced expression evaluation with a validated numeric discount rate. |
| Shell command constructed from filename | Security — High | 58 | os.system() passes a filename into a shell command, creating injection risk. | Removed shell execution and used print() for the status message. |
| Hardcoded secret printed | Security — Low (Bandit) | 70, 74 | A string resembling an API secret is hardcoded and printed. | Removed the unused secret and its print statement. |
| Weak MD5 hash | Security — High (Bandit) | 47 | MD5 is unsuitable when a cryptographically secure hash is required. | Replaced MD5 with SHA-256 for the member ID digest. |
| Insecure PIN generation | Security — Low | 51 | random is not intended for security-sensitive random values. | Used secrets to generate a four-digit PIN. |
| Mutable default list | Reliability | 14 | A default list can be shared between function calls. | Used None and created a list inside the function when needed. |
| Bare exception | Reliability | 26 | A bare except hides unrelated errors during membership cancellation. | Caught KeyError and returned False when the member does not exist. |
| Unused imports and variables | Maintainability | 6, 31, 41, 58 | Unused names obscure the program's purpose and trigger analyzer warnings. | Removed unused names and used the renewal base fee in the calculation. |
| File resource handling | Reliability | 55 | The file is opened and closed manually, and encoding is unspecified. | Used a with statement and UTF-8 encoding. |
| Naming and documentation | Maintainability | 15, 23, 30, 40 | Function names do not follow snake_case and docstrings are missing. | Renamed functions and added docstrings. |
| Formatting and final newline | Style | 10, 11, 18, 82 | Long lines and a missing final newline trigger style warnings. | Reformatted the file and added a final newline. |
