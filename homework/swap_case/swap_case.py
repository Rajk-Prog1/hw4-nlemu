def swap_case(s: str) -> int:
    lista = []
    for k in s:
        if k.isupper():
            lista.append(k.lower())
        elif k.islower:
            lista.append(k.upper())
        else:
            lista.append(k)
    s = "".join(lista)
    print(s)

# ezekkel van tesztelve
# nekem úgy tűnik, hogy lefutnak és swapcase-elnek, de a teszt mégse működik

# swap_case("22T6M2reD4")
# swap_case("HackerRank.com presents 'Pythonist 2'.")
"""swap_case(
                "SG.2ehL62pSmsnd7c9XYYsFvV067gybBhsSM0SJ7zpAJWr8pwEFzq3ACtuSAjpL7ZnWXbASGlBnEawSnWs1 gpCySKB2.at bt5S"
            )"""

""""swap_case(
               "K96.5GI.sabDH3s.6iFzxMAh5IPtmWJ4w0uJ9MOWC45eoZkhaSs73gxKoQcd90Uge02cAxPnyMWtYW'TRVcO.0VnBq.sIQ5HFhkx"
            )"""

"""swap_case(
                "hG4 KIm2ONx3x5epersw Dz.ytOVfXSxrh'MephUyRYAkHsDZOZStP'2XRv6XqcT0RkI5INrfr38 4BPUuS85OGWXNgXZPaHF1oy"
            ) """
""""
swap_case(
                "OzD0ro.7xwq A.MqhqT7'evgaVjpQ36OjSwfhuMaME'SDlyjPttjr6knZURciDARzAZ.3hQeIvX'IPe875zS3su6dajlMnbQOiH37U3YG0uzy6vW4v.onodBDDREYOf3CqeHfGcCeWV0dXrmTWAUsuw'jVwFO'5n.jvKLwXaDsam'y5sVQqB5O16bn1ug1XFeg3kmOGQFjxQ524k Z0yv76b4kkaC YuW9cw8Sfjf4 ynhe N88N3N2pfJF.I4ec5PgTp0Mp6VKawzg7GctsbPmU73aERqHxvWOMxDGZI9XWnJV6Aumecv0bHopAmfeD1K vTcxkzmdypHOGcdELdXjINde.ICPhEnpr9nJVL M7uY'L0BDX0i7CNCjIt9OiE2xjXt7JkK7vdUFlp6qn3Zua5vfP'nJcbviLrwj3.VlDDkd4VQ6zV1G2sGMmTVYkzaR9z5CDujAl'zYw8jw 9VOb5dP'zT'UTLMX2u8OG5YrGrvcENXF'QhBC8Ti'KRuhuO'SLlDKuRPHxFtnXW27YY1BMN9YkQww9kloEb43'loYiSFpIPiA0f1.3RYNUEN4QSbNQMpwQPZXsVKhc.uGvGJHiU80gcvOufOI2A0LdPcwGBWjTDl4TBZaycMfCmOceYqPj gqV7wTfSkY1F4INWqlKez.Vzbf84htDJg6D4MUt 2cGy8gMQolE 3gLR.rh3s5nbzN8hqKJr4c0L48zm2Hm7ObgsDu8dlrHnDaVKLQ65a7oTyz D6MLYD.q2AQXnQHKuTxKu5Fq7iNIRZKYyYeZo8n8JwHXtDbOaEnu'4'vmAsf2XR2q0ozLdw2FVsVpKEm4KzigoxY2GOpZq3OYW8cboQoD7STPJ8B'yEGZgk0vT mBABj0xeckqn6'Ouo"
            )
"""
