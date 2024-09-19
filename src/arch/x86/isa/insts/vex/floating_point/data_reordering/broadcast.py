microcode = '''
def macroop VEX_VBROADCASTSS_XMM_XMM {
    gem5_avx_broadcast xmm, xmmm, size=4, ext=XMM
};

def macroop VEX_VBROADCASTSS_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_broadcast xmm, uvec1, size=4, ext=XMM
};

def macroop VEX_VBROADCASTSS_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_broadcast xmm, uvec1, size=4, ext=XMM
};

def macroop VEX_VBROADCASTSS_YMM_XMM {
    gem5_avx_broadcast ymm, xmmm, size=4, ext=YMM
};

def macroop VEX_VBROADCASTSS_YMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_broadcast  ymm, uvec1, size=4, ext=YMM
};

def macroop VEX_VBROADCASTSS_YMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_broadcast ymm, uvec1, size=4, ext=YMM
};

def macroop VEX_VBROADCASTSD_YMM_XMM {
    gem5_avx_broadcast ymm, xmmm, size=8, ext=YMM
};

def macroop VEX_VBROADCASTSD_YMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_broadcast ymm, uvec1, size=8, ext=YMM
};

def macroop VEX_VBROADCASTSD_YMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_broadcast ymm, uvec1, size=8, ext=YMM
};

def macroop VEX_VBROADCASTF128_YMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VBROADCASTF128_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_broadcast_pd ymm, uvec1, size=8, ext="2 |" + YMM
};

def macroop VEX_VBROADCASTF128_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_broadcast_pd ymm, uvec1, size=8, ext="2 |" + YMM
};

'''
