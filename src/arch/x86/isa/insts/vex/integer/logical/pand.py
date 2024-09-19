microcode = '''
def macroop VEX_VPAND_XMM_XMM_XMM {
    gem5_avx_and_epu64 xmm1, xmm2, xmmm, size=16, ext=XMM
};

def macroop VEX_VPAND_XMM_XMM_M {
    lea t1, seg, sib, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_and_epu64 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop VEX_VPAND_XMM_XMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_and_epu64 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop VEX_VPANDN_XMM_XMM_XMM {
    gem5_avx_andn_epu64 xmm1, xmm2, xmmm, size=16, ext=XMM
};

def macroop VEX_VPANDN_XMM_XMM_M {
    lea t1, seg, sib, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_andn_epu64 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop VEX_VPANDN_XMM_XMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_andn_epu64 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop VEX_VPAND_YMM_YMM_YMM {
    gem5_avx_and_epu64 ymm1, ymm2, ymmm, size=32, ext=YMM
};

def macroop VEX_VPAND_YMM_YMM_M {
    lea t1, seg, sib, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_and_epu64 ymm1, ymm2, uvec1, size=32, ext=YMM
};

def macroop VEX_VPAND_YMM_YMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_and_epu64 ymm1, ymm2, uvec1, size=32, ext=YMM
};

def macroop VEX_VPANDN_YMM_YMM_YMM {
    gem5_avx_andn_epu64 ymm1, ymm2, ymmm, size=32, ext=YMM
};

def macroop VEX_VPANDN_YMM_YMM_M {
    lea t1, seg, sib, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_andn_epu64 ymm1, ymm2, uvec1, size=32, ext=YMM
};

def macroop VEX_VPANDN_YMM_YMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_andn_epu64 ymm1, ymm2, uvec1, size=32, ext=YMM
};

def macroop VEX_KANDW_K_K_K {
    gem5_avx_kand k1, k2, km, size=2, ext=0
};

def macroop VEX_KANDNW_K_K_K {
    gem5_avx_kandn k1, k2, km, size=2, ext=0
};

def macroop VEX_KNOTW_K_K {
    gem5_avx_knot k1, km, size=2, ext=0
};

'''
