from itertools import count
import time
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# membuat atribut PID yang dapat diperbaharui dalam loop
class ControlSimulation:
    def __init__(self):
        self.state =  0
        self.prevT, self.eprev, self.eintegral = 0, 0, 0

    @staticmethod
    def clamp(n, minn, maxn):
        if n < minn:
            return minn
        elif n > maxn:
            return maxn
        else:
            return n

    # membuat fungsi PID yang mengembalikan nilai u, e, dedt, eintegral, state, target agar bisa dipanggil untuk plotting realtime
    def PID(self, kp, ki, kd, target):
        #   // time difference
        self.currT = time.time()
        time.sleep(0.001)
        self.prevT = time.time()
        deltaT = ((self.currT - self.prevT))
        #   // error
        e = self.state-target
        #   // derivative
        dedt = (e-self.eprev)/(deltaT)
        #   // integral
        self.eintegral = self.eintegral + e*deltaT
        #   // control signal
        u = kp*e + kd*dedt + ki*self.eintegral
        #   // store previous error
        eprev = e
        #   // control
        if min(-100, u)<0:
            self.state -= self.system(u)
        if  max(100, u)>0:
            self.state -= self.system(u)
        # mengembalikan nilai
        return u, e, dedt, self.eintegral, self.state, target

    def customPID(self, kp, ki, kd, target, state):
        #   // time difference
        self.currT = time.time()
        time.sleep(0.001)
        self.prevT = time.time()
        deltaT = ((self.currT - self.prevT))
        #   // error
        newState = state
        e = newState-target
        #   // derivative
        dedt = (e-self.eprev)/(deltaT)
        #   // integral
        self.eintegral = self.eintegral + e*deltaT
        #   // control signal
        u = kp*e + kd*dedt + ki*self.eintegral
        #   // store previous error
        eprev = e
        #   // control
        if min(-100, u)<0:
            newState -= self.system(u)
        if  max(100, u)>0:
            newState -= self.system(u)
        # mengembalikan nilai
        # print(u, self.system)
        return newState

    def simulation(self, kp=1, ki=0, kd=0 , target=200):
        
        """
        fungsi simulation(a,b,c,d) akan menjalankan grafik realtime simulasi kontrol PID yang dilakukan
        > memiliki keterangan parameter opsional berupa
            a : konstanta proporsional, default = 1
            b : konstanta integral, default = 0
            c : konstanta derevatif, default = 0
            d : nilai setpoint/target, default = 200

        fungsi system(u) adalah fungsi alih yang dimiliki sistem/plant dimana parameter u tidak digunakan
        fungsi system dapat diganti dengan fungsi polinomial biasa
        """

        # membuat nilai x secara otomatis
        index = count()
        x = []
        # mendefinisikan variabel array untuk diplotting
        uArr, eArr, dedtArr, eintegralArr, varArr, tarArr = [], [], [], [], [], []
        # fungsi animasi
        def animate(i):
            # menaruh nilai pid pada variabel sementara
            temp = self.PID(kp,ki,kd, target)
            # memasukan nilai realtime pada array yang sudah dibuat
            x.append(next(index))
            eArr.append(temp[1])
            varArr.append(temp[4])
            uArr.append(temp[0])
            tarArr.append(temp[5])
            # melakukan clear plot
            plt.cla()
            # menggambar garis pada figure
            plt.plot(x, varArr, label='State',  linewidth=1)
            plt.plot(x, tarArr, label='Target',  linewidth=1)
            plt.plot(x, eArr, label='Error',  linewidth=1)
            plt.legend(loc='lower right')
            # menjalankan fungsi agar figure terlihat semua (responsif)
            plt.tight_layout()
        # memanggil fungsi dasar untuk plotting realtime
        ani = FuncAnimation(plt.gcf(), animate, interval = 1)
        # menampilkan figure
        plt.tight_layout()
        plt.show()

    # mendefinisikan sistem (plant)
    @staticmethod
    def system(u):
        return (0.23*u**2 + 6.12*u + 2.12 + 23.92* u**-1)/(10.21*u + 3.12)

robot = ControlSimulation().simulation(30, 0.5, 0.001, 2000)
# state = 0
# for i in range(8):
#     state = ControlSimulation().customPID(10, 0.01, 0.04, 1000, state)
#     print(state)