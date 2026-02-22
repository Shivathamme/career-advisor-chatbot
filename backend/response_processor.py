def process_response(response_text:str) -> str:
    """
    Cleans and validates Gemini response before displaying to UI.
    """
    if not response_text:
        return "Sorry, I could not generate a response.please try again."
    
    # Remove unnecessary leading/trailing whitespace
    cleaned_response = response_text.strip()
    
    return cleaned_response