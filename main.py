import datetime
from fpdf import FPDF
A4_WIDTH = 210
A4_HEIGHT = 297

def vowel_start(word):
    if word[0] in ['a','e','i','o','u']:
        return True
    return False

def cover_letter(params):
    '''
        1) TODO: format TEMPLATE cover letter below to own personal experience
    '''
    TEMPLATE = f"""{params["date"]}
{params["recruiter_name"]}
{params["position"]}
{params["company"]}
{params["company_address"]}
{params["location_params"]}
Subject: {params["position"]} with {params["company"]} (Job ID: {params["id"]})
Dear {params["salutation"] + ". " if params["salutation"] else ""}{params["recruiter_name"]},
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam in mauris lectus. Curabitur ut facilisis est. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed velit risus, pulvinar et placerat id {"an" if vowel_start(params["position"]) else "a"} {params["position"]}, duis eleifend tincidunt sapien. Mauris laoreet purus ante {params["company"]} nunc malesuada id justo vitae accumsan. Nam pharetra orci et pretium elementum {params["company"]}'s ligula ipsum egestas ex. Duis vel varius odio {params["company"]}'s pharetra vitae dolor vel, venenatis gravida neque {params["mission_statement_keywords"]}.
Nullam sodales ex sit amet vehicula tincidunt. Quisque in aliquet velit, at aliquet diam. Cras porttitor lacinia ipsum id bibendum. Nulla luctus massa a pulvinar molestie. Fusce aliquet vel velit et iaculis. Cras at arcu venenatis, feugiat est ut, ornare ligula. Duis vel ullamcorper enim. Etiam mattis tellus in finibus placerat. Etiam quis convallis metus.
Vestibulum facilisis magna a maximus dapibus. Curabitur sodales massa in justo convallis, eu gravida sapien fringilla. Quisque imperdiet, arcu vel laoreet bibendum, diam nisi commodo leo, eget elementum sem metus in tellus. Integer egestas accumsan neque id tincidunt. Vestibulum non orci id purus ornare luctus.
Donec viverra mi sit amet ipsum lobortis finibus {"an" if vowel_start(params["position"]) else "a"} {params["position"]}.

Aenean vel finibus ipsum,
Sed a urna at tortor,
Efe Harmankaya
    """
    return TEMPLATE

class PDF(FPDF):
    def header(self):
        # Setup template background
        self.image('coop_cover_letter_template.png', 0, 0, A4_WIDTH, A4_HEIGHT - 10)
        self.ln(20)

def main():
    '''
        2) TODO: Change values in 'params' below based on posting data
    '''
    # Setup cover letter parameters
    params = {
        'date' : str(datetime.date.today()),
        'id' : 'POST_ID',
        'recruiter_name' : 'RECRUITER NAME',
        'position' : 'POSITION',
        'company' : 'COMPANY',
        'company_address' : 'ADDRESS',
        'location_params' : 'LOCATION',
        'salutation' : 'Mr',
        'mission_statement_keywords' : 'COMPANY SPECIFIC'
    }

    # Setup PDF environment
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    
    # Construct letter with input params and write to PDF
    text = cover_letter(params).encode('latin-1', 'replace').decode('latin-1').split('\n')
    for sentence in text:
        pdf.multi_cell(0, 7, sentence, 0, 'L')
        pdf.ln(2)
    pdf.output(f'cover_letters/cover_letter_{params["id"]}_{params["company"].split(" ")[0]}.pdf', 'F')


if __name__ == '__main__':
    main()

    