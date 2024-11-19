import requests

def execute_code_with_jdoodle(client_id, client_secret, code, detected_language):
    # Map detected language to JDoodle parameters
    jdoodle_language_map = {
        "python": {"language": "python3", "versionIndex": "4"},
        "java": {"language": "java", "versionIndex": "4"},
        "c": {"language": "c", "versionIndex": "5"},
        "cpp": {"language": "cpp17", "versionIndex": "0"},
        "javascript": {"language": "nodejs", "versionIndex": "4"},
    }

    # Get the JDoodle parameters for the detected language
    if detected_language not in jdoodle_language_map:
        return f"Unsupported language: {detected_language}"

    jdoodle_params = jdoodle_language_map[detected_language]

    # Prepare the payload
    payload = {
        "clientId": client_id,
        "clientSecret": client_secret,
        "script": code,
        "language": jdoodle_params["language"],
        "versionIndex": jdoodle_params["versionIndex"],
    }

    # JDoodle API endpoint
    api_url = "https://api.jdoodle.com/v1/execute"

    # Make the POST request
    response = requests.post(api_url, json=payload)

    # Return the result
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage
client_id = "125184c99c2f92c5402b9ecb7a46e2e7"
client_secret = "68d1d4c4c1d96d252cc69a0df6499a448a5f83500071934cb88e49af4eed50c3"
code = """

console.log("hello world")

"""  # Example Python code
detected_language = "javascript"

output = execute_code_with_jdoodle(client_id, client_secret, code, detected_language)
print(output)
