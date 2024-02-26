import os

from email_extractor import extract_emails, save_extracted_emails


def test_extract_multiple_emails(get_test_abspath):
    """
    Test that emails are correctly extracted from an image.
    """
    input_image_path = get_test_abspath("tests/images/multiple_emails.webp")
    expected_emails = [
        "c.nick@ahrefs.com",
        "churick.n@ahrefs.com",
        "churick.nick@ahrefs.com",
        "churick@ahrefs.com",
        "churickn@ahrefs.com",
        "churicknick@ahrefs.com",
        "cnick@ahrefs.com",
        "n.c@ahrefs.com",
        "n.churick@ahrefs.com",
        "nc@ahrefs.com",
        "nchurick@ahrefs.com",
        "nick.c@ahrefs.com",
        "nick.churick@ahrefs.com",
        "nick@ahrefs.com",
        "nickc@ahrefs.com",
        "nickchurick@ahrefs.com",
    ]

    extracted_emails = extract_emails(input_image_path)
    assert sorted(extracted_emails) == sorted(expected_emails), "Extracted emails do not match expected emails."


def test_save_extracted_emails(get_test_abspath):
    """
    Test that extracted emails are correctly saved to a file.
    """
    output_file_path = get_test_abspath("tests/images/test_output.txt")
    test_emails = ["test1@example.com", "test2@example.com"]

    # Ensure output file does not exist before test
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    save_extracted_emails(test_emails, output_file_path)

    assert os.path.exists(output_file_path), "Output file was not created."

    with open(output_file_path, "r") as file:
        content = file.read()
        for email in test_emails:
            assert email in content, f"{email} not found in output file."

    # Cleanup after test
    os.remove(output_file_path)
