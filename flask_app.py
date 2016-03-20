from flask import Flask, render_template, request

cipher_table = []
base = 32

# creating the cipher table
for index in range(0, 95):
    curr_list = range(index, index + 95)

    # fixing the list
    curr_list = map(lambda x: chr(base + (x % 95)), curr_list)

    # adding the new list to the table
    cipher_table.append(curr_list)


# encrypting the message by key
def encrypt_msg(key, msg):
    msg_list = list(msg)

    encrypted_msg = ""

    # creating a list of locations for each key's letter alphabet
    key_chars = map(lambda x: ord(x) - base, list(key))

    # encrypting the message
    for loc in range(len(msg_list)):
        curr_char = msg_list[loc]

        char = ord(curr_char) - base

        # the alphabet to encrypt based on the key current char
        alphabet = key_chars[loc % len(key_chars)]

        # adding the encrypted char to the message
        encrypted_msg += cipher_table[alphabet][char]

    return encrypted_msg


# decrypting the message by key
def decrypt_msg(key, msg):
    msg_list = list(msg)

    decrypted_msg = ""

    # creating a list of locations for each key's letter alphabet
    key_chars = map(lambda x: ord(x) - base, list(key))

    # encrypting the message
    for loc in range(len(msg_list)):
        curr_char = msg_list[loc]

        # the alphabet to encrypt based on the key current char
        alphabet = key_chars[loc % len(key_chars)]

        # decrypting the char to the original message
        decrypted_msg += chr(base + cipher_table[alphabet].index(curr_char))

    return decrypted_msg


app = Flask(__name__, static_folder='static', static_url_path='/static')


def encrypt_user_msg(key, msg):
    ans = encrypt_msg(key, msg)
    return render_template('msg_encrypted.html', key=key, org_msg=msg, enc_msg=ans)


def decrypt_user_msg(key, msg):
    ans = decrypt_msg(key, msg)
    return render_template('msg_decrypted.html', key=key, org_msg=msg, dec_msg=ans)


@app.route("/")
def root():
    # return app.send_static_file('index.html')
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.route('/code', methods=['POST', 'GET'])
def code():
    error = None
    if request.method == 'POST':
        # 0 - encrypt | 1 - decrypt
        act = request.form['act']
        key = request.form['key']
        msg = request.form['msg']

        # assuming the input validation preformed on the HTML page
        if act == '0':
            return encrypt_user_msg(key, msg)
        else:
            return decrypt_user_msg(key, msg)

    else:
        error = 'There was a problem with your input, please try again.'
        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return render_template('error.html', error=error)


if __name__ == "__main__":
    app.run()

