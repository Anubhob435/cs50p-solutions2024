# extensions.py

def main():
    # Prompt the user for the name of a file
    file_name = input("File name: ").strip().lower()

    # Determine the file's media type based on its extension
    media_type = get_media_type(file_name)

    # Output the media type
    print(media_type)

def get_media_type(file_name):
    """
    This function returns the media type based on the file's extension.
    If the extension is not recognized, it returns 'application/octet-stream'.
    """
    # Dictionary mapping file extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Check the file's extension
    for ext, media in media_types.items():
        if file_name.endswith(ext):
            return media

    # Default media type
    return "application/octet-stream"

if __name__ == "__main__":
    main()
