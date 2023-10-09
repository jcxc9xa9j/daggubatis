import json

# Read JSON data from Familytree.md file in the current working directory
with open("Familytree.md", "r") as file:
    json_data = json.load(file)

# Create the HTML code with the JSON data
html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Daggibatis</title>
    <style>
        /* Set the iframe to fill the entire screen */
        iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none; /* Remove iframe border */
        }}
    </style>
</head>
<body>
    <!-- JSONCrack Embed iframe -->
    <iframe id="jsoncrackEmbed" src="https://jsoncrack.com/widget"></iframe>

    <script>
        const jsonCrackEmbed = document.querySelector("iframe");

        // Sample JSON data (replace this with your JSON data)
        const json_data = {json_data};

        // Convert JSON data to a string
        const jsonData = JSON.stringify(json_data);

        // Function to update iframe dimensions when the window is resized
        function updateIframeDimensions() {{
            jsonCrackEmbed.style.height = window.innerHeight + "px";
        }}

        // Initial iframe dimensions
        updateIframeDimensions();

        // Send the JSON data to the embedded JSONCrack iframe
        window.addEventListener("message", (event) => {{
            jsonCrackEmbed.contentWindow.postMessage({{ json: jsonData }}, "*");
        }});

        // Update iframe dimensions when the window is resized
        window.addEventListener("resize", updateIframeDimensions);
    </script>
</body>
</html>
"""

# Save the HTML code to a file
with open("../index.html", "w") as output_file:
    output_file.write(html_code)

print("HTML code generated and saved to 'index.html'")
