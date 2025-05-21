# LaunchDarkly Workshop: Feature Flags in Practice

A hands-on workshop and presentation for learning about feature flags in practice, using Flask, LaunchDarkly, and Slidev.

---

## 🚀 Project Overview

- **Workshop**: Presentation slides and a live demo Flask app to illustrate feature flag concepts.
- **Live Demo**: See how feature flags can control user experience in real time.
- **DIY**: Use as a follow-along or as a template for your own feature flag experiments.

---

## 🐍 Python Project Management

- **Maintainers:**  
  This project uses [Rye](https://rye-up.com/) for Python environment and dependency management.
  - Install Rye: [Rye Quickstart](https://rye-up.com/guide/installation/)
  - Install dependencies:  
    ```sh
    rye sync
    ```
  - Run the Flask app (with auto-reload):  
    ```sh
    rye run dev
    ```
    (This runs `flask --app app run --debug` as defined in `pyproject.toml`.)

- **Users:**  
  You can also use plain Python:
  ```sh
  pip install -r requirements.lock
  flask --app app run --debug
  ```

---

## 🦄 Feature Flag Demo (Flask)

- The app serves a simple landing page at `/`.
- **Feature flag logic** (using LaunchDarkly) is included but commented out by default.
- To enable LaunchDarkly:
  1. Uncomment the relevant code in `app.py`.
  2. Set the `LD_SDK_KEY` environment variable.
  3. Create a flag named `show_next_landing` in your LaunchDarkly project.

---

## 🖼️ Presentation Slides (Slidev)

- The workshop slides are in [`slides.md`](slides.md).
- To present or view locally:
  1. Install Slidev: [Slidev Installation Guide](https://sli.dev/guide/install.html)
  2. Run:
     ```sh
     npx slidev
     ```
  3. Open the provided local URL in your browser.

---

## 📁 Project Structure

```
.
├── app.py                  # Flask app (feature flag demo)
├── templates/
│   ├── landing.html        # Default landing page
│   └── landing_next.html   # Alternate page (for flag demo)
├── static/
│   └── styles.css          # Shared CSS
├── slides.md               # Slidev presentation
├── pyproject.toml          # Python project config (Rye)
├── requirements.lock       # Python dependencies
└── README.md
```

---

## 🛠️ Customization & Extending

- Add your own feature flags and templates to extend the demo.
- Use the project as a starting point for your own workshops or experiments.

---

## 📝 Notes

- **No tests yet**—PRs welcome!
- The LaunchDarkly integration is disabled by default for easy setup.
- Rye is recommended for maintainers, but not required for users.

---

## 📚 Resources

- [Rye Python Tool](https://rye-up.com/)
- [Slidev Presentation Tool](https://sli.dev/)
- [LaunchDarkly Docs](https://docs.launchdarkly.com/)
