def summarizer(data,chat,query=False):
    overall_response = chat.send_message(f"summarize this as a researcher who have many years of experiance {data}")
    if query:
        return overall_response
    else:
        section_summary=chat.send_message(f"give summery of each section separately{data}" )
        oneline_summary=chat.send_message(f"give a oneline summary{data}" )
        final_summary=chat.send_message(f"summarize this as a researcher with atleast {str(overall_response)+str(section_summary)+str(oneline_summary)}",stream=True )
        return final_summary
def highlights(data,chat):
    data_highlights = chat.send_message(f"highlights key points maximum atleast 10 to 50{data}",stream=True)
    return data_highlights
 
def chatbot(input,summary,chat):
    response= chat.send_message(f"Ans this Question {input} in this Context {summary} ",stream=True)
    return response