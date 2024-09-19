microcode = '''
def macroop VEX_VCVTPS2DQ_XMM_XMM {
    gem5_avx_cvtps_epi32 xmm, xmmm, size=4, ext="4 |" + XMM
};

def macroop VEX_VCVTPS2DQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtps_epi32 xmm, uvec1, size=4, ext="4 |" + XMM
};

def macroop VEX_VCVTPS2DQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtps_epi32 xmm, uvec1, size=4, ext="4 |" + XMM
};

def macroop VEX_VCVTPD2DQ_XMM_XMM {
    gem5_avx_cvtpd_epi32 xmm, xmmm, srcSize=8, destSize=4, ext="4 |" + XMM
};

def macroop VEX_VCVTPD2DQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtpd_epi32 xmm, uvec1, srcSize=8, destSize=4, ext="4 |" + XMM
};

def macroop VEX_VCVTPD2DQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtpd_epi32 xmm, uvec1, srcSize=8, destSize=4, ext="4 |" + XMM
};

def macroop VEX_VCVTTPS2DQ_XMM_XMM {
    gem5_avx_cvtps_epi32 xmm, xmmm, size=4, ext=XMM
};

def macroop VEX_VCVTTPS2DQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtps_epi32 xmm, uvec1, size=4, ext=XMM
};

def macroop VEX_VCVTTPS2DQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtps_epi32 xmm, uvec1, size=4, ext=XMM
};

def macroop VEX_VCVTPS2DQ_YMM_YMM {
    gem5_avx_cvtps_epi32 ymm, ymmm, size=4, ext="4 |" + YMM
};

def macroop VEX_VCVTPS2DQ_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtps_epi32 ymm, uvec1, size=4, ext="4 |" + YMM
};

def macroop VEX_VCVTPS2DQ_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtps_epi32 ymm, uvec1, size=4, ext="4 |" + YMM
};

def macroop VEX_VCVTPD2DQ_XMM_YMM {
    gem5_avx_cvtpd_epi32 xmm, ymmm, srcSize=8, destSize=4, ext="4 |" + YMM
};

def macroop VEX_VCVTPD2DQ_XMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtpd_epi32 xmm, uvec1, srcSize=8, destSize=4, ext="4 |" + YMM
};

def macroop VEX_VCVTPD2DQ_XMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtpd_epi32 xmm, uvec1, srcSize=8, destSize=4, ext="4 |" + YMM
};

def macroop VEX_VCVTTPS2DQ_YMM_YMM {
    gem5_avx_cvtps_epi32 ymm, ymmm, size=4, ext=YMM
};

def macroop VEX_VCVTTPS2DQ_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtps_epi32 ymm, uvec1, size=4, ext=YMM
};

def macroop VEX_VCVTTPS2DQ_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtps_epi32 ymm, uvec1, size=4, ext=YMM
};

def macroop VEX_VCVTTPD2DQ_XMM_XMM {
   gem5_avx_cvtpd_epi32 xmm, xmmm, srcSize=8, destSize=4, ext=XMM
};

def macroop VEX_VCVTTPD2DQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtpd_epi32 xmm, uvec1, srcSize=8, destSize=4, ext=XMM
};

def macroop VEX_VCVTTPD2DQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtpd_epi32 xmm, uvec1, srcSize=8, destSize=4, ext=XMM
};

def macroop VEX_VCVTTPD2DQ_XMM_YMM {
    gem5_avx_cvtpd_epi32 xmm, ymmm, srcSize=8, destSize=4, ext=YMM
};

def macroop VEX_VCVTTPD2DQ_XMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtpd_epi32 xmm, uvec1, srcSize=8, destSize=4, ext=YMM
};

def macroop VEX_VCVTTPD2DQ_XMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtpd_epi32 xmm, uvec1, srcSize=8, destSize=4, ext=YMM
};

'''
