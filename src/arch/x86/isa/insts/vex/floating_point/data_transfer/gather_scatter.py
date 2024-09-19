microcode = '''
def macroop VEX_VGATHERDPS_XMM_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERDPS_XMM_XMM_M {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu32 uvec1, uvec1, uvec1, size=4, ext=XMM
loadLoopTop:
    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=4
    gem5_avx_set_epi32 uvec1, uvec1, t2, t4, size=4, ext=0
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_avx_move_epu32 xmm, uvec1, size=4, ext=XMM
    fault "NoFault"
};

def macroop VEX_VGATHERDPS_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERDPS_YMM_YMM_YMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERDPS_YMM_YMM_M {
    limm t3, 8, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu32 uvec1, uvec1, uvec1, size=4, ext=YMM
loadLoopTop:
    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=4
    gem5_avx_set_epi32 uvec1, uvec1, t2, t4, size=4, ext=0
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_avx_move_epu32 ymm, uvec1, size=4, ext=YMM
    fault "NoFault"
};

def macroop VEX_VGATHERDPS_YMM_YMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERQPS_XMM_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERQPS_XMM_XMM_M {
    limm t3, 2, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu32 uvec1, uvec1, uvec1, size=4, ext=XMM
loadLoopTop:
    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=4
    gem5_avx_set_epi32 uvec1, uvec1, t2, t4, size=4, ext=0
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_avx_move_epu32 xmm, uvec1, size=4, ext=XMM
    fault "NoFault"
};

def macroop VEX_VGATHERQPS_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERQPS_YMM_YMM_YMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERQPS_YMM_YMM_M {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu32 uvec1, uvec1, uvec1, size=4, ext=YMM
loadLoopTop:
    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=4
    gem5_avx_set_epi32 uvec1, uvec1, t2, t4, size=4, ext=0
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_avx_move_epu32 ymm, uvec1, size=4, ext=YMM
    fault "NoFault"
};

def macroop VEX_VGATHERQPS_YMM_YMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERDPD_XMM_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERDPD_XMM_XMM_M {
    limm t3, 2, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu64 uvec1, uvec1, uvec1, size=8, ext=XMM
loadLoopTop:
    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=8
    gem5_avx_set_epi64 xmm, xmm, t2, t4, size=8, ext=0
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_avx_move_epu64 xmm, uvec1, size=8, ext=XMM
    fault "NoFault"
};

def macroop VEX_VGATHERDPD_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERDPD_YMM_YMM_YMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERDPD_YMM_YMM_M {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu64 uvec1, uvec1, uvec1, size=8, ext=YMM
loadLoopTop:
    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=8
    gem5_avx_set_epi64 ymm, ymm, t2, t4, size=8, ext=0
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_avx_move_epu64 ymm, uvec1, size=8, ext=YMM
    fault "NoFault"
};

def macroop VEX_VGATHERDPD_YMM_YMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERQPD_XMM_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERQPD_XMM_XMM_M {
    limm t3, 2, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu64 uvec1, uvec1, uvec1, size=8, ext=XMM
loadLoopTop:
    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=8
    gem5_avx_set_epi64 xmm, xmm, t2, t4, size=8, ext=0
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_avx_move_epu64 xmm, uvec1, size=8, ext=XMM
    fault "NoFault"
};

def macroop VEX_VGATHERQPD_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERQPD_YMM_YMM_YMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VGATHERQPD_YMM_YMM_M {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu64 uvec1, uvec1, uvec1, size=8, ext=YMM
loadLoopTop:
    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=8
    gem5_avx_set_epi64 ymm, ymm, t2, t4, size=8, ext=0
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_avx_move_epu64 ymm, uvec1, size=8, ext=YMM
    fault "NoFault"
};

def macroop VEX_VGATHERQPD_YMM_YMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

'''
