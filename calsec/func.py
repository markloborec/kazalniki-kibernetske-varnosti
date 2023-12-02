import datetime

from calsec import vec



def SPS(Tmeasure: list[float],
        Wmesaure: list[float],
        ResultMTBI: float,
        WMTBI: float = 1,
        C: float = 10):
    """
    SPS: As a key indicator of the effectiveness of controls in cyber security in protection
    transmission and distribution network or of its work, which can be a smart grid,
    the strategic performance indicator 𝑆𝑃𝑆 is used.
    Given the parameters in the function, the maximum value of SPS is 1 and the minimum value is 0.
    :param C: Normalization constant = 10
    :param Tmeasure: the weighting factor of the influence of the OIMTBI indicator
    :param Wmesaure: the weighting factor of the influence of the WMeasure indicator
    :param ResultMTBI: the value of the indicator ResultMTBI
    :param WMTBI:the weighting factor of OIMTBI
    :return: SPS Value
    """
    up = (sum(vec.multi(Tmeasure, Wmesaure)) + (ResultMTBI * WMTBI * C))
    down = sum(Wmesaure) + WMTBI
    return 1 / C * up / down


def TNPPS(Resultmeasure: list[float],
          Wmeasure: list[float],
          C: float = 10):
    """

    :param Resultmeasure: Mesaures the result of the (Maximummesaure - Averagemesaure)/(Maximummeasure - Minmesaure)
    :param Wmeasure: Is the list of WMCME, WMCMU, WMCNP. All have the value of 5.
    :param C:  Normalization constant = 10
    :return: The value of the TNPPS Cybersecurity Indicator.
    """
    up = sum(vec.multi(Resultmeasure, Wmeasure))
    down = sum(Wmeasure)
    return C * up / down


def TNPPS_OLMCME(
        MEcounterm: list[float]):
    """

    :param MEcounterm: Monthly incident number from harmful emails
    :return: Returns the value of OLMCME
    """
    up = sum(MEcounterm)
    down = len(MEcounterm)
    return up / down


def TNPPS_OLMCMU(
        MUcounterm: list[float]):
    """

    :param MUcounterm: Monthly incident number from harmful URL
    :return: Returns the value of OLMCMU
    """
    up = sum(MUcounterm)
    down = len(MUcounterm)
    return up / down


def TNPPS_OLMCNP(
        NPcounterm: list[float]):
    """

    :param NPcounterm: Monthly incident number from network intrusions
    :return: Returns the value of OLMCNP
    """
    up = sum(NPcounterm)
    down = len(NPcounterm)
    return up / down

def TNPPS_ONMAPS(
        MAPScounterm: list[float]):
    """

    :param MAPScounterm: Monthly incident number from network intrusions
    :return: Returns the value of OLMCNP
    """
    APRezultatdos = lambda nN07,Maxdos = 10,Mindos = 0: (Maxdos - nN07)/(Maxdos-Mindos)
    up = sum([APRezultatdos(np) for np in MAPScounterm])
    down = abs(len(MAPScounterm))
    return up / down



################################################

def TEPS(Resultmeasure: float,
         Wmeasure: list[float],
         C: float = 10):
    """

    :param Resultmeasure: Mesaures the result of the (Maximummesaure - Averagemesaure)/(Maximummeasure - Minmesaure)
    :param Wmeasure: Is the list of WMCMW, WMCMD, WMCSD. All have the value of 5.
    :param C:  Normalization constant = 10
    :return: The value of the TEPS Cybersecurity Indicator.
    """
    up = sum(vec.skal_multi(Wmeasure, Resultmeasure))
    down = sum(Wmeasure)
    return C * up / down


def TEPS_OLMCMW(
        MWcounterm: list[float]):
    """

    :param MWcounterm: Monthly incident number from harmful emails
    :return: Returns the value of OLMCMW
    """
    up = sum(MWcounterm)
    down = len(MWcounterm)
    return up / down


def TEPS_OLMCMD_SD(
        MDSDcounterm: list[float]):
    """

    :param MDSDcounterm: Monthly incident on final points of omrežje
    :return: Returns the value of OLMDMD
    """
    up = sum(MDSDcounterm)
    down = len(MDSDcounterm)
    return up / down




###########################################
def THSS(Resultmeasure: float,
         Wmeasure: list[float],
         C: float = 10):
    """

    :param Resultmeasure: Mesaures the result of the (Maximummesaure - Averagemesaure)/(Maximummeasure - Minmesaure)
    :param Wmeasure: Is the list of WMCSE, WMCHR. All have the value of 2.
    :param C:  Normalization constant = 10
    :return: The value of the THSS Cybersecurity Indicator.
    """
    up = sum(vec.skal_multi(Wmeasure,Resultmeasure))
    down = sum(Wmeasure)
    return C * up / down


def THSS_OLMCSE(
        SEcounterm: list[float]):
    """

    :param SEcounterm: Monthly incident number from harmful emails
    :return: Returns the value of OLMCSE
    """
    up = sum(SEcounterm)
    down = len(SEcounterm)
    return up / down


def THSS_OLMCHR(
        HRcounterm: list[float]):
    """

    :param HRcounterm: Monthly incident number from harmful emails
    :return: Returns the value of OLMCHR
    """
    up = sum(HRcounterm)
    down = len(HRcounterm)
    return up / down


##################################

def OIMTBI(I: list[datetime.date]):
    """
    :param I: The list of any incidents
    :return I: Average number of days between incidents
    """
    I.sort()
    d_days = []
    for i in range(len(I) - 1):
        current = I[i]
        next = I[i + 1]
        d_days.append((next - current).days)
    return sum(d_days) / len(d_days)
