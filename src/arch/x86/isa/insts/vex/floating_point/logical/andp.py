microcode = '''
def macroop VEX_VANDPS_XMM_XMM_XMM {
    gem5_avx_and_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VANDPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
   gem5_avx_and_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VANDPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_and_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VANDPS_YMM_YMM_YMM {
    gem5_avx_and_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VANDPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_and_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VANDPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_and_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VANDPD_XMM_XMM_XMM {
    gem5_avx_and_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VANDPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_and_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VANDPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_and_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VANDPD_YMM_YMM_YMM {
    gem5_avx_and_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VANDPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_and_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VANDPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_and_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VANDNPS_XMM_XMM_XMM {
    gem5_avx_andn_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VANDNPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_andn_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VANDNPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_andn_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VANDNPS_YMM_YMM_YMM {
    gem5_avx_andn_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VANDNPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_andn_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VANDNPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_andn_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VANDNPD_XMM_XMM_XMM {
    gem5_avx_andn_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VANDNPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_andn_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VANDNPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_andn_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VANDNPD_YMM_YMM_YMM {
    gem5_avx_andn_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VANDNPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_andn_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VANDNPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_andn_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_ANDN_R_R_R
{
    andn reg1, reg2, regm, flags=(OF,SF,ZF,PF,CF)
};

def macroop VEX_ANDN_R_R_M
{
    ldst t1, seg, sib, disp
    andn reg1, reg2, t1, flags=(OF,SF,ZF,PF,CF)
};

def macroop VEX_ANDN_R_R_P
{
    rdip t7
    ldst t1, seg, riprel, disp
    andn reg1, reg2, t1, flags=(OF,SF,ZF,PF,CF)
};

'''
