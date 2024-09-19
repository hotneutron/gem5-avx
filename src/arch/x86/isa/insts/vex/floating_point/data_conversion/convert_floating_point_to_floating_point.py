microcode = '''
def macroop VEX_VCVTSS2SD_XMM_XMM_XMM {
    gem5_avx_cvtss_sd xmm1, xmm2, xmmm, destSize=8, srcSize=4, ext=0
};

def macroop VEX_VCVTSS2SD_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_cvtss_sd xmm1, xmm2, uvec1, destSize=8, srcSize=4, ext=0
};

def macroop VEX_VCVTSS2SD_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_cvtss_sd xmm1, xmm2, uvec1, destSize=8, srcSize=4, ext=0
};

def macroop VEX_VCVTSD2SS_XMM_XMM_XMM {
    gem5_avx_cvtsd_ss xmm1, xmm2, xmmm, destSize=4, srcSize=8, ext=Scalar
};

def macroop VEX_VCVTSD2SS_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_cvtsd_ss xmm1, xmm2, uvec1, destSize=4, srcSize=8, ext=Scalar
};

def macroop VEX_VCVTSD2SS_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_cvtsd_ss xmm1, xmm2, uvec1, destSize=4, srcSize=8, ext=Scalar
};

def macroop VEX_VCVTPS2PD_XMM_XMM {
    gem5_avx_cvtps_pd xmm, xmmm, destSize=8, srcSize=4, ext=XMM
};

def macroop VEX_VCVTPS2PD_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_cvtps_pd xmm, uvec1, destSize=8, srcSize=4, ext=XMM
};

def macroop VEX_VCVTPS2PD_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_cvtps_pd xmm, uvec1, destSize=8, srcSize=4, ext=XMM
};

def macroop VEX_VCVTPS2PD_YMM_XMM {
    gem5_avx_cvtps_pd ymm, xmmm, destSize=8, srcSize=4, ext=YMM
};

def macroop VEX_VCVTPS2PD_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_cvtps_pd ymm, uvec1, destSize=8, srcSize=4, ext=YMM
};

def macroop VEX_VCVTPS2PD_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_cvtps_pd ymm, uvec1, destSize=8, srcSize=4, ext=YMM
};

def macroop VEX_VCVTPD2PS_XMM_XMM {
    gem5_avx_cvtpd_ps xmm, xmmm, destSize=4, srcSize=8, ext=XMM
};

def macroop VEX_VCVTPD2PS_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtpd_ps xmm, uvec1, destSize=4, srcSize=8, ext=XMM
};

def macroop VEX_VCVTPD2PS_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtpd_ps xmm, uvec1, destSize=4, srcSize=8, ext=XMM
};

def macroop VEX_VCVTPD2PS_XMM_YMM {
    gem5_avx_cvtpd_ps ymm, ymmm, destSize=4, srcSize=8, ext=YMM
};

def macroop VEX_VCVTPD2PS_XMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtpd_ps ymm, uvec1, destSize=4, srcSize=8, ext=YMM
};

def macroop VEX_VCVTPD2PS_XMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtpd_ps ymm, uvec1, destSize=4, srcSize=8, ext=YMM
};

'''
