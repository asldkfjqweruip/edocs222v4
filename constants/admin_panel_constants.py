from datetime import datetime


class AdminPanelConstants:
    TASKTYPS = '//*[@href="#!/admin/taskTypes"]'
    CREATETASKTYPS = '//*[@id="registry-splitting-container"]/section/ui-view/div/div[2]/a'
    TTFIELD = '/html/body/div[4]/md-dialog/form/md-dialog-content/md-input-container[1]/input'
    TEXT = f'автотест поле {str(datetime.today())}'
    BUTTONSAVE = './/*[@class="btn save-button"]'
    REOPENCRATED = f'//*[text()="{TEXT}"]'
    DELETE = '//*[class="btn btn-danger delete-button"]'
    DELETEFULL = '/html/body/div[4]/md-dialog/form/md-dialog-actions/div/div[1]/button'
    BASICK = '//*[@id="registry-item-row-id-21"]/td[2]/button'
    BASICK2 = '//*[@id="registry-item-row-id-31"]/td[2]/button'
    REQUIREDACTIONS = '/html/body/div[4]/md-dialog/form/md-dialog-content/md-input-container[4]/div/md-chips/md-chips-wrap/div/div/md-autocomplete/md-autocomplete-wrap/input'
    REGISTRATION = '/html/body/md-virtual-repeat-container[1]/div/div[2]/ul/li[1]'
    QRCODE = '/html/body/md-virtual-repeat-container[1]/div/div[2]/ul/li[8]'
    STAMPORSING = '/html/body/md-virtual-repeat-container[1]/div/div[2]/ul/li[7]'
    CLOSE = '/html/body/div[4]/md-dialog/form/md-toolbar/div/button'
    ERRORTEXT = '/html/body/div[4]/md-dialog/form/md-dialog-content/div[5]'