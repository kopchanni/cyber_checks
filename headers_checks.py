import requests

domain = ''


def check_headers(domain: str):
    re = requests.get(url='https://'+domain).headers
    # print(re)


    header_checks = ['X-Frame-Options', 'Strict-Transport_Security', 'X-Content-Type-Options',
                     'Content-Security-Policy', 'X-Frame-Options', 'X-XSS-Protection',
                     'Referrer-Policy', 'Feature-Policy']

    for head in header_checks:
        if head in re:
            with open('headers_output.txt', 'w') as file:
                file.write(domain + 'No threats')
            # print(domain + 'No threats')
        elif head not in re:
            with open('headers_output.txt', 'w') as file:
                file.write(domain + " Header Threat(s): " + head)
            # print('------------------------------------')
            # print(domain + " Header Threat(s): " + head)

