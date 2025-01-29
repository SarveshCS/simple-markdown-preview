# Markdown Preview Application

This is a simple Markdown preview application built with Flask. It allows users to write Markdown text and see a live preview of the rendered HTML. The application supports both light and dark themes.

## Features

- Live Markdown preview
- Theme switching (light and dark)
- Responsive design

## Project Structure

```
markdown-preview-app
├── static
│   ├── base.css          # Base styles 
│   ├── dark-theme.css    # Dark theme styles
│   ├── home.css          # Styles for the home page
│   ├── light-theme.css    # Light theme styles
│   └── navbar.css        # Styles for the navigation bar
├── templates
│   ├── base.html         # Base HTML template
│   ├── home.html         # Home page template
│   └── navbar.html       # Navigation bar template
├── app.py                # Main application file
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd markdown-preview-app
   ```

2. Install the required packages:
   ```
   pip install Flask markdown
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000`.

## Usage

- Write your Markdown content in the editor on the home page.
- The preview will update in real-time as you type.
- Use the buttons in the navigation bar to switch between light and dark themes.

## License

This project is open-source and available under the MIT License.