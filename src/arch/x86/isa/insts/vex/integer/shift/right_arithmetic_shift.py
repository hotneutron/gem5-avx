microcode = '''
def macroop VEX_VPSRAW_XMM_XMM_XMM {
    gem5_avx_sra_epi16 xmm1, xmm2, xmmm, size=2, ext=XMM
};

def macroop VEX_VPSRAW_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_sra_epi16 xmm1, xmm2, uvec1, size=2, ext=XMM
};

def macroop VEX_VPSRAW_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_sra_epi16 xmm1, xmm2, uvec1, size=2, ext=XMM
};

def macroop VEX_VPSRAW_XMM_XMM_I {
    gem5_avx_srai_epi16i xmm1, xmmm, imm, size=2, ext=XMM
};

def macroop VEX_VPSRAW_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_srai_epi16i xmm1, uvec1, imm, size=2, ext=XMM
};

def macroop VEX_VPSRAW_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_srai_epi16i xmm1, uvec1, imm, size=2, ext=XMM
};

def macroop VEX_VPSRAW_YMM_YMM_XMM {
    gem5_avx_sra_epi16 ymm1, ymm2, xmmm, size=2, ext=YMM
};

def macroop VEX_VPSRAW_YMM_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_sra_epi16 ymm1, ymm2, uvec1, size=2, ext=YMM
};

def macroop VEX_VPSRAW_YMM_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_sra_epi16 ymm1, ymm2, uvec1, size=2, ext=YMM
};

def macroop VEX_VPSRAW_YMM_YMM_I {
    gem5_avx_srai_epi16i ymm1, ymmm, imm, size=2, ext=YMM
};

def macroop VEX_VPSRAW_YMM_M_I {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_srai_epi16i ymm1, uvec1, imm, size=2, ext=YMM
};

def macroop VEX_VPSRAW_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_srai_epi16i ymm1, uvec1, imm, size=2, ext=YMM
};

def macroop VEX_VPSRAD_XMM_XMM_XMM {
    gem5_avx_sra_epi32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPSRAD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_sra_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPSRAD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_sra_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPSRAD_XMM_XMM_I {
    gem5_avx_srai_epi32i xmm1, xmmm, imm, size=4, ext=XMM
};

def macroop VEX_VPSRAD_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_srai_epi32i xmm1, uvec1, imm, size=4, ext=XMM
};

def macroop VEX_VPSRAD_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_srai_epi32i xmm1, uvec1, imm, size=4, ext=XMM
};

def macroop VEX_VPSRAD_YMM_YMM_XMM {
    gem5_avx_sra_epi32 ymm1, ymm2, xmmm, size=4, ext=YMM
};

def macroop VEX_VPSRAD_YMM_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_sra_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPSRAD_YMM_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_sra_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPSRAD_YMM_YMM_I {
    gem5_avx_srai_epi32i ymm1, ymmm, imm, size=4, ext=YMM
};

def macroop VEX_VPSRAD_YMM_M_I {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_srai_epi32i ymm1, uvec1, imm, size=4, ext=YMM
};

def macroop VEX_VPSRAD_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_srai_epi32i ymm1, uvec1, imm, size=4, ext=YMM
};

'''
