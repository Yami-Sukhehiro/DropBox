import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f= open(file_from, 'rb')
        dbx.files_upload(f.read() , file_to)

def main():
    access_token = 'sl.A_UxtMmQo5_OxL8QSLJBed7tb1dTKjjQiVkA3vZiX4xL1-wZoa3sT5lOWFTsfHSRJd5wfZy0lczmxqyYxos_IAKcYs_ipVPN30skMTzHZIesIsRvSgvLNs-1L4KKXNw6gF2gmz4'
    transfer = TransferData(access_token)
    file_from = input ("enter the damn file you wanna transfer dumbass")
    file_to = input("Drop the Dropbox path")
    transfer.upload_files(file_from,file_to)
    print('Yur File has moved to WAKANDA!')        
main()
