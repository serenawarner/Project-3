def search_feature(data, keyword):
    """
    Searches for a keyword in a collection of note records and returns matching file names and count.

    Args: 
        data: iterable - Each item should be a tuple or dict containing 'filename' and 'content'
        keyword: str - keyword to search for

    Returns: 
        tuple: (list of matching filenames, count of matches)
    """
    matching_files = []

    for record in data:
        # Support both tuple (filename, content) and dict {'filename': ..., 'content': ...}
        if isinstance(record, dict):
            filename = record.get("filename")
            content = record.get("content", "")
        else:
            filename, content = record

        if keyword.lower() in content.lower():
            matching_files.append(filename)

    num_matches = len(matching_files)

    print(f"{num_matches} file(s) have been found containing the keyword '{keyword}'.")
    if matching_files:
        print("File names:")
        for name in matching_files:
            print(f" - {name}")

    return matching_files, num_matches