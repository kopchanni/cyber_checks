import sys
import tkinter
# import nmap as n
import os
import re
from paths import *
from headerscheck import *
from io import StringIO

# import _dirbpy.URLBruteforcer as dirb


# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# Regular Expression Pattern to extract the number of ports you want to scan.
# You have to specify <lowest_port_number>-<highest_port_number> (ex 10-100)
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535

# output saved from cmd
# https://www.windowscentral.com/how-save-command-output-file-using-command-prompt-or-powershell

def cyber_checks_automation(input):

    os.system("ping " + input + f' > {main_dir}')


    with open('output_file.txt', 'rt') as file:
        content = file.read()

    ip = f'{content[20:34]}'
    print(ip)
    print('CONDUCTING CYBER_CHECKS')

    # with open(f'output{hostname}', 'r') as
    #     sys.stdout = open(f'output_{hostname_1}', 'w')
    # print('----------------------------------------------------------------------------------------------')
    # print('ADDITIONAL COMMANDS')
    print('CONDUCTING OS detection')
    os_detect = os.system(f'nmap -O {ip} >> {main_dir}')
    # print(os_detect)
    # print('===============================================================================================')
    print('CONDUCTING TCP SYN Scan')
    tcp_syn_scan = os.system(f'nmap -sS {ip} >> {main_dir}')
    # print(tcp_syn_scan)
    # print('===============================================================================================')
    # print('Scan UDP ports') # taking to much time
    # os.system(f'nmap -sU {ip_add_entered}')
    # print('===============================================================================================')
    # print('----------------------------------------------------------------------------------------------')
    # print('Sub-net Host discovery') # taking to much time
    # os.system(f'nmap -sV -T4 {ip_add_entered}/24')
    # print('----------------------------------------------------------------------------------------------')
    print('CONDUCTING HEADERS SECURITY CHECKS')
    check_headers(domain=input)
    print('CHECKS COMPLETED')


if __name__ == '__main__':
    hostname = "rebiz.com"  # example
    hostname_1 = 'idcleveland.com'

    main_window = tkinter.Tk()
    main_window.geometry('300x100')
    main_window.title('CYBERCHECKS')
    domain_entry = tkinter.Label(master=main_window,
                                 text='ENTER DOMAIN / URL').grid(row=0)
    domain_input = tkinter.Entry(main_window)
    domain_input.grid(row=0, column=1)
    # input_url = domain_input.get()

    # os.system('ping ' + input_url + f' > {main_dir}')
    start_button = tkinter.Button(master=main_window,
                                command=lambda: cyber_checks_automation(input=str(domain_input.get())),
                                  text='START CHECKS', fg='green')
    start_button.grid(row=1, column=1)
    main_window.mainloop()

    # print(ip)
    
    print('CHECK OUTPUT RESULTS IN THE FOLLOWING DIR')
    print('NMAP RESULTS: ' + main_dir)
    print('HEADERS RESULTS: ' + main_dir_1)
    print('END OF SCRIPT')
