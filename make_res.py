import urllib
import urllib2


def login(memberemail, memberpin):
    page = "http://www.worldclass.ro/includes/ajax/login-user.php"
    email = memberemail
    pin = memberpin

    raw_params = {'email': email, 'pin': pin}
    params = urllib.urlencode(raw_params)
    req = urllib2.Request(page, params)
    page = urllib2.urlopen(req)
    cookies = page.info()['Set-Cookie']
    page.close()
    # find start of the PHPSESSID cookie
    start = cookies.index('=')
    #find the end of the PHPSESSID cookie
    end = cookies.index(' ')
    return cookies[start + 1:end - 1]


def make_reservation(cookie, classid, email, pin):
    page = 'http://www.worldclass.ro/includes/ajax/_book_class.php'
    classid = classid
    centerid = 402
    memberemail = email
    memberpin = pin
    outlook = "undefined"
    clubname = "Health Academy at the Grand"

    raw_params = {'classId': classid, 'centerId': centerid, 'memberEmail': memberemail, 'memberPin': memberpin,
                  'outlook': outlook, 'clubName': clubname}

    # use cookies here
    cookies = urllib.urlencode({'PHPSESSID': cookie})
    params = urllib.urlencode(raw_params)
    headers = {'Cookie': cookies}

    req = urllib2.Request(page, params, headers)
    page = urllib2.urlopen(req)
    print page.read()


def main():
    memberemail = "random@random.com"
    memberpin = 1234
    classid = 7890
    cookie = login(memberemail, memberpin)

    make_reservation(cookie, classid, memberemail, memberpin)


if __name__ == '__main__':
    main()
