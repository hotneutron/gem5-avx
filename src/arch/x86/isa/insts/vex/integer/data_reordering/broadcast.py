microcode = '''
def macroop VEX_VPBROADCASTB_XMM_XMM {
    gem5_avx_broadcast xmm, xmmm, size=1, ext=XMM
};

def macroop VEX_VPBROADCASTB_YMM_XMM {
    gem5_avx_broadcast ymm, xmmm, size=1, ext=YMM
};

def macroop VEX_VPBROADCASTB_ZMM_XMM {
    gem5_avx_broadcast zmm, xmmm, size=1, ext=ZMM
};

def macroop VEX_VPBROADCASTW_XMM_XMM {
    gem5_avx_broadcast xmm, xmmm, size=2, ext=XMM
};

def macroop VEX_VPBROADCASTW_YMM_XMM {
    gem5_avx_broadcast ymm, xmmm, size=2, ext=YMM
};

def macroop VEX_VPBROADCASTW_ZMM_XMM {
    gem5_avx_broadcast zmm, xmmm, size=2, ext=ZMM
};

def macroop VEX_VPBROADCASTD_XMM_XMM {
    gem5_avx_broadcast xmm, xmmm, size=4, ext=XMM
};

def macroop VEX_VPBROADCASTD_YMM_XMM {
    gem5_avx_broadcast ymm, xmmm, size=4, ext=YMM
};

def macroop VEX_VPBROADCASTD_ZMM_XMM {
    gem5_avx_broadcast zmm, xmmm, size=4, ext=ZMM
};

def macroop VEX_VPBROADCASTQ_XMM_XMM {
    gem5_avx_broadcast xmm, xmmm, size=8, ext=XMM
};

def macroop VEX_VPBROADCASTQ_YMM_XMM {
    gem5_avx_broadcast ymm, xmmm, size=8, ext=YMM
};

def macroop VEX_VPBROADCASTQ_ZMM_XMM {
    gem5_avx_broadcast zmm, xmmm, size=8, ext=ZMM
};

'''

sibRel = 'ld t1, seg, sib, disp, dataSize={}'
pcRel = '''rdip t7
    ld t1, seg, riprel, disp, dataSize={}'''

vpbroadcast_code = '''
def macroop VEX_VPBROADCAST%(type)s_%(vec)s_%(suffix)s {
    %(readOp1)s
    gem5_avx_set1 %(op1)s, %(op2)s, size=%(size)s, ext=\"1 | \" + %(vec)s
};
'''

for (optype,opsize) in [('B','1'), ('W','2'), ('D','4'), ('Q','8')]:
    for vec in ['XMM', 'YMM']:
        for (suffix, readOp1, op2) in [('R','','regm'), ('M',sibRel,'t1'), ('P',pcRel,'t1')]:
            microcode += vpbroadcast_code % {"type": optype, "vec": vec,
                    "suffix": suffix, "readOp1": readOp1.format(opsize), "op1": vec.lower(),
                    "op2": op2, "size": opsize}

