import config
from crypto import JCCrypto

def run():
    # Get configuration environment, it could be adapted in the future for case where you have multiple environments
    conf = config.Config

    # Create a instance from JCCrypto class
    crypto = JCCrypto(
        conf.TOKEN,
        conf.URL_BASE,
        conf.GET_EXT,
        conf.POST_EXT,
        conf.FILE_PATH
    )

    # Get the json file and persist it in Disk
    crypto.persist_to_json(
        crypto.get_json_from_url()
    )

    # create variable with decrypt message
    decrypt_val = crypto.decrypt(
                    crypto.get_json_info('cifrado'),
                    crypto.get_json_info('numero_casas')
                  )

    # create variable with the hash for decrypted message
    encrypt_summary = crypto.encrypt_summary(decrypt_val)

    # update json file, setting decrypted message and summary (hash from decrypted message)
    crypto.set_json_info("decrifrado", decrypt_val)
    crypto.set_json_info("resumo_criptografico", encrypt_summary)

    # send file to API
    crypto.send_json_file()

if __name__ == '__main__':
    run()