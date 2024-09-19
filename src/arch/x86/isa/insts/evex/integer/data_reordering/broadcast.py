microcode = '''
def macroop EVEX_VPBROADCASTMB2Q_XMM_K {
    gem5_avx_broadcastmb_epi64 xmm, km, size=4, ext=XMM
};

def macroop EVEX_VPBROADCASTMB2Q_YMM_K {
    gem5_avx_broadcastmb_epi64 ymm, km, size=4, ext=YMM
};

def macroop EVEX_VPBROADCASTMB2Q_ZMM_K {
    gem5_avx_broadcastmb_epi64 zmm, km, size=4, ext=ZMM
};

def macroop EVEX_VPBROADCASTMW2D_XMM_K {
    gem5_avx_broadcastmw_epi32 xmm, km, size=4, ext=XMM
};

def macroop EVEX_VPBROADCASTMW2D_YMM_K {
    gem5_avx_broadcastmw_epi32 ymm, km, size=4, ext=YMM
};

def macroop EVEX_VPBROADCASTMW2D_ZMM_K {
    gem5_avx_broadcastmw_epi32 zmm, km, size=4, ext=ZMM
};

def macroop EVEX_VBROADCASTI32X2_XMM_XMM {
    gem5_avx_broadcast_ps xmm, xmmm, size=4, ext="2 |" + XMM
};

def macroop EVEX_VBROADCASTI32X2_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_broadcast_ps xmm, uvec1, size=4, ext="2 |" + XMM
};

def macroop EVEX_VBROADCASTI32X2_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_broadcast_ps xmm, uvec1, size=4, ext="2 |" + XMM
};

def macroop EVEX_VBROADCASTI32X2_YMM_XMM {
    gem5_avx_broadcast_ps ymm, xmmm, size=4, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTI32X2_YMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_broadcast_ps ymm, uvec1, size=4, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTI32X2_YMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_broadcast_ps ymm, uvec1, size=4, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTI32X2_ZMM_XMM {
    gem5_avx_broadcast_ps zmm, xmmm, size=4, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTI32X2_ZMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTI32X2_ZMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTI32X4_YMM_XMM {
    gem5_avx_broadcast_ps ymm, xmmm, size=4, ext="4 |" + YMM
};

def macroop EVEX_VBROADCASTI32X4_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_broadcast_ps ymm, uvec1, size=4, ext="4 |" + YMM
};

def macroop EVEX_VBROADCASTI32X4_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_broadcast_ps ymm, uvec1, size=4, ext="4 |" + YMM
};

def macroop EVEX_VBROADCASTI32X4_ZMM_XMM {
    gem5_avx_broadcast_ps zmm, xmmm, size=4, ext="4 |" + ZMM
};

def macroop EVEX_VBROADCASTI32X4_ZMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="4 |" + ZMM
};

def macroop EVEX_VBROADCASTI32X4_ZMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="4 |" + ZMM
};

def macroop EVEX_VBROADCASTI64X2_YMM_XMM {
    gem5_avx_broadcast_pd ymm, xmmm, size=8, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTI64X2_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_broadcast_pd ymm, uvec1, size=8, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTI64X2_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_broadcast_pd ymm, uvec1, size=8, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTI64X2_ZMM_XMM {
    gem5_avx_broadcast_pd zmm, xmmm, size=8, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTI64X2_ZMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_broadcast_pd zmm, uvec1, size=8, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTI64X2_ZMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_broadcast_pd zmm, uvec1, size=8, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTI32X8_ZMM_YMM {
    gem5_avx_broadcast_ps zmm, ymmm, size=4, ext="8 |" + ZMM
};

def macroop EVEX_VBROADCASTI32X8_ZMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="8 |" + ZMM
};

def macroop EVEX_VBROADCASTI32X8_ZMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="8 |" + ZMM
};

def macroop EVEX_VBROADCASTI64X4_ZMM_YMM {
    gem5_avx_broadcast_pd zmm, ymmm, size=8, ext="4 |" + ZMM
};

def macroop EVEX_VBROADCASTI64X4_ZMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_broadcast_pd zmm, uvec1, size=8, ext="4 |" + ZMM
};

def macroop EVEX_VBROADCASTI64X4_ZMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_broadcast_pd zmm, uvec1, size=8, ext="4 |" + ZMM
};

'''

sibRel = 'ld t1, seg, sib, disp'
pcRel = '''rdip t7
    ld t1, seg, riprel, disp'''

vpbroadcast_code = '''
def macroop EVEX_VPBROADCAST%(type)s_%(vec)s_%(suffix)s {
    %(readOp1)s
    gem5_avx_set1 %(op1)s, %(op2)s, size=%(size)s, ext=\"1 | \" + %(vec)s
};

def macroop EVEX_VPBROADCAST%(type)s_%(vec)s_%(suffix)s_K {
    %(readOp1)s
    gem5_mask_set1 %(op1)s, %(op2)s, opmask=opmask, src2=%(op1)s, size=%(size)s, ext=\"1 | \" + %(vec)s
};
'''

for (optype,opsize) in [('B','1'), ('W','2'), ('D','4'), ('Q','8')]:
    for vec in ['XMM', 'YMM', 'ZMM']:
        for (suffix, readOp1, op2) in [('R','','regm'), ('M',sibRel,'t1'), ('P',pcRel,'t1')]:
            microcode += vpbroadcast_code % {"type": optype, "vec": vec,
                    "suffix": suffix, "readOp1": readOp1, "op1": vec.lower(),
                    "op2": op2, "size": opsize}


VEC_sibRel = 'ldvec128lo0 uvec1, seg, sib, disp, dataSize=8'
VEC_pcRel = '''rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8'''

vpbroadcast_code = '''
def macroop EVEX_VPBROADCAST%(type)s_%(vec)s_%(suffix)s {
    %(readOp1)s
    gem5_avx_broadcast %(op1)s, %(op2)s, size=%(size)s, ext=%(vec)s
};

def macroop EVEX_VPBROADCAST%(type)s_%(vec)s_%(suffix)s_K {
    %(readOp1)s
    gem5_mask_broadcast %(op1)s, %(op2)s, opmask=opmask, src2=%(op1)s, size=%(size)s, ext=%(vec)s
};
'''

for (optype,opsize) in [('B','1'), ('W','2'), ('D','4'), ('Q','8')]:
    for vec in ['XMM', 'YMM', 'ZMM']:
        for (suffix, readOp1, op2) in [('XMM','','xmmm'), ('M',VEC_sibRel,'uvec1'), ('P',VEC_pcRel,'uvec1')]:
            microcode += vpbroadcast_code % {"type": optype, "vec": vec,
                    "suffix": suffix, "readOp1": readOp1, "op1": vec.lower(),
                    "op2": op2, "size": opsize}
