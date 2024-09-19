microcode = '''
def macroop EVEX_VPGATHERDD_XMM_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERDD_XMM_M_K {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu32 uvec1, uvec1, uvec1, size=4, ext=XMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=4
    gem5_avx_set_epi32 uvec1, uvec1, t2, t4, size=4, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERDD_XMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERDD_YMM_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERDD_YMM_M_K {
    limm t3, 8, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu32 uvec1, uvec1, uvec1, size=4, ext=YMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=4
    gem5_avx_set_epi32 uvec1, uvec1, t2, t4, size=4, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERDD_YMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERDD_ZMM_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERDD_ZMM_M_K {
    limm t3, 16, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu32 uvec1, uvec1, uvec1, size=4, ext=ZMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=4
    gem5_avx_set_epi32 uvec1, uvec1, t2, t4, size=4, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERDD_ZMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERDQ_XMM_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERDQ_XMM_M_K {
    limm t3, 2, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu64 uvec1, uvec1, uvec1, size=8, ext=XMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=8
    gem5_avx_set_epi64 uvec1, uvec1, t2, t4, size=8, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERDQ_XMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERDQ_YMM_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERDQ_YMM_M_K {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu64 uvec1, uvec1, uvec1, size=8, ext=YMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=8
    gem5_avx_set_epi64 uvec1, uvec1, t2, t4, size=8, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERDQ_YMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERDQ_ZMM_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERDQ_ZMM_M_K {
    limm t3, 8, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu64 uvec1, uvec1, uvec1, size=8, ext=ZMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=8
    gem5_avx_set_epi64 uvec1, uvec1, t2, t4, size=8, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERDQ_ZMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQD_XMM_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQD_XMM_M_K {
    limm t3, 2, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu32 uvec1, uvec1, uvec1, size=4, ext=XMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=4
    gem5_avx_set_epi32 uvec1, uvec1, t2, t4, size=4, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERQD_XMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQD_YMM_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQD_YMM_M_K {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu32 uvec1, uvec1, uvec1, size=4, ext=YMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=4
    gem5_avx_set_epi32 uvec1, uvec1, t2, t4, size=4, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERQD_YMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQD_ZMM_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQD_ZMM_M_K {
    limm t3, 8, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu32 uvec1, uvec1, uvec1, size=4, ext=ZMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=4
    gem5_avx_set_epi32 uvec1, uvec1, t2, t4, size=4, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERQD_ZMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQQ_XMM_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQQ_XMM_M_K {
    limm t3, 2, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu64 uvec1, uvec1, uvec1, size=8, ext=XMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=8
    gem5_avx_set_epi64 uvec1, uvec1, t2, t4, size=8, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERQQ_XMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQQ_YMM_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQQ_YMM_M_K {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu64 uvec1, uvec1, uvec1, size=8, ext=YMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=8
    gem5_avx_set_epi64 uvec1, uvec1, t2, t4, size=8, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERQQ_YMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQQ_ZMM_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPGATHERQQ_ZMM_M_K {
    limm t3, 8, dataSize=8
    limm t4, 0, dataSize=8
    gem5_avx_xor_epu64 uvec1, uvec1, uvec1, size=8, ext=ZMM
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=0
    ld t2, seg, [scale, t1, base], disp, dataSize=8
    gem5_avx_set_epi64 uvec1, uvec1, t2, t4, size=8, ext=0
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    gem5_mask_move_epu64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
    fault "NoFault"
};

def macroop EVEX_VPGATHERQQ_ZMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDD_XMM_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDD_M_XMM_K {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=Signed
    gem5_avx_get_epi32 t2, xmm, t4, size=4, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=4
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERDD_P_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDD_YMM_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDD_M_YMM_K {
    limm t3, 8, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=Signed
    gem5_avx_get_epi32 t2, ymm, t4, size=4, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=4
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERDD_P_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDD_ZMM_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDD_M_ZMM_K {
    limm t3, 16, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=Signed
    gem5_avx_get_epi32 t2, zmm, t4, size=4, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=4
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERDD_P_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDQ_XMM_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDQ_M_XMM_K {
    limm t3, 2, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=Signed
    gem5_avx_get_epi64 t2, xmm, t4, size=8, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=8
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERDQ_P_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDQ_YMM_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDQ_M_YMM_K {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=Signed
    gem5_avx_get_epi64 t2, ymm, t4, size=8, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=8
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERDQ_P_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDQ_ZMM_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERDQ_M_ZMM_K {
    limm t3, 8, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi32 t1, vindex, t4, size=4, ext=Signed
    gem5_avx_get_epi64 t2, zmm, t4, size=8, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=8
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERDQ_P_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQD_XMM_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQD_M_XMM_K {
    limm t3, 2, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=Signed
    gem5_avx_get_epi32 t2, xmm, t4, size=4, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=4
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERQD_P_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQD_YMM_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQD_M_YMM_K {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=Signed
    gem5_avx_get_epi32 t2, ymm, t4, size=4, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=4
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERQD_P_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQD_ZMM_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQD_M_ZMM_K {
    limm t3, 8, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=Signed
    gem5_avx_get_epi32 t2, zmm, t4, size=4, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=4
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERQD_P_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQQ_XMM_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQQ_M_XMM_K {
    limm t3, 2, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=Signed
    gem5_avx_get_epi64 t2, xmm, t4, size=8, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=8
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERQQ_P_XMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQQ_YMM_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQQ_M_YMM_K {
    limm t3, 4, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=Signed
    gem5_avx_get_epi64 t2, ymm, t4, size=8, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=8
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERQQ_P_YMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQQ_ZMM_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPSCATTERQQ_M_ZMM_K {
    limm t3, 8, dataSize=8
    limm t4, 0, dataSize=8
loadLoopTop:
    maskbit opmask, t4, flags=(EZF,)
    br label("skipLoop"), flags=(CEZF,)

    gem5_avx_get_epi64 t1, vindex, t4, size=8, ext=Signed
    gem5_avx_get_epi64 t2, zmm, t4, size=8, ext=0
    st t2, seg, [scale, t1, base], disp, dataSize=8
skipLoop:
    addi t4, t4, 1
    subi t3, t3, 1, flags=(EZF,), dataSize=8
    br label("loadLoopTop"), flags=(nCEZF,)
end:
    fault "NoFault"
};

def macroop EVEX_VPSCATTERQQ_P_ZMM_K {
    fault "std::make_shared<UnimpInstFault>()"
};

'''
