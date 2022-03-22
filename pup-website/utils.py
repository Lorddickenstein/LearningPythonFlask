import os

def read_files(folder='web/static/files/', file_name='None'):
    content = []
    f = None
    if file_name:
        try:
            f = open(folder + file_name, 'r')
            for line in f:
                if file_name == 'departments.txt':
                    dep_id, desc = line.strip().split(', ')
                    content.append({
                        'dep_id': dep_id,
                        'description': desc
                    })
                elif file_name == 'subjects.txt':
                    sub_code, year_level, desc, units = line.strip().split(', ')
                    content.append({
                        'sub_code': sub_code,
                        'year_level': year_level,
                        'description': desc,
                        'units': units
                    })
                elif file_name == 'students.txt':
                    stud_num, section, department, is_enrolled, no_of_subs, fname, mname, lname, address, age, sex, email, birthday, password = line.strip().split(', ')
                    content.append({
                        'stud_num': stud_num,
                        'section': section,
                        'department': department,
                        'is_enrolled': is_enrolled,
                        'no_of_subs': no_of_subs,
                        'fname': fname,
                        'mname': mname,
                        'lname': lname,
                        'address': address,
                        'age': age,
                        'sex': sex,
                        'email': email,
                        'birthday': birthday,
                        'password': password
                    })
                elif file_name == 'admins.txt':
                    admin_num, fname, mname, lname, address, age, sex, email, birthday, password = line.strip().split(', ')
                    content.append({
                        'admin_num': admin_num,
                        'fname': fname,
                        'mname': mname,
                        'lname': lname,
                        'address': address,
                        'age': age,
                        'sex': sex,
                        'email': email,
                        'birthday': birthday,
                        'password': password
                    })
                    
        except FileNotFoundError as exc:
            content = []
            print(exc)
        finally:
            if f is not None: f.close()

    return content