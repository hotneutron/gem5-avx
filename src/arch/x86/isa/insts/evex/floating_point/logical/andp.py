microcode = '''
def macroop EVEX_VANDPS_XMM_XMM_XMM {
    gem5_avx_and_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VANDPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
   gem5_avx_and_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VANDPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_and_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VANDPS_YMM_YMM_YMM {
    gem5_avx_and_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VANDPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_and_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VANDPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_and_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VANDPS_ZMM_ZMM_ZMM {
    gem5_avx_and_epu32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VANDPS_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_and_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VANDPS_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_and_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VANDPD_XMM_XMM_XMM {
    gem5_avx_and_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VANDPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_and_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VANDPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_and_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VANDPD_YMM_YMM_YMM {
    gem5_avx_and_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VANDPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_and_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VANDPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_and_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VANDPD_ZMM_ZMM_ZMM {
    gem5_avx_and_epu64 zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VANDPD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_and_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VANDPD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_and_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VANDNPS_XMM_XMM_XMM {
    gem5_avx_andn_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VANDNPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_andn_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VANDNPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_andn_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VANDNPS_YMM_YMM_YMM {
    gem5_avx_andn_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VANDNPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_andn_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VANDNPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_andn_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VANDNPS_ZMM_ZMM_ZMM {
    gem5_avx_andn_epu32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VANDNPS_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_andn_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VANDNPS_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_andn_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VANDNPD_XMM_XMM_XMM {
    gem5_avx_andn_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VANDNPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_andn_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VANDNPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_andn_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VANDNPD_YMM_YMM_YMM {
    gem5_avx_andn_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VANDNPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_andn_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VANDNPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_andn_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VANDNPD_ZMM_ZMM_ZMM {
    gem5_avx_andn_epu64 zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VANDNPD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_andn_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VANDNPD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_andn_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

'''
