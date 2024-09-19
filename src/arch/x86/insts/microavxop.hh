/*
 * Copyright (c) 2009 The Regents of The University of Michigan
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met: redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer;
 * redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution;
 * neither the name of the copyright holders nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef __ARCH_X86_INSTS_MICROAVXOP_HH__
#define __ARCH_X86_INSTS_MICROAVXOP_HH__

#include "arch/x86/insts/microop.hh"

namespace X86ISA
{
    enum AVXFlag {
        AVXMultHiOp = 1,
        AVXSignedOp = 64,
        AVXScalarOp = 128,
        AVXXMMOp = 256,
        AVXYMMOp = 512,
        AVXZMMOp = 1024
    };

    class AVXOpBase : public X86MicroopBase
    {
      protected:
        const RegIndex src1;
        const RegIndex dest;
        const uint8_t srcSize;
        const uint8_t destSize;
        const uint16_t ext;
        static const RegIndex foldOBit = 0;

        // Constructor
        AVXOpBase(ExtMachInst _machInst,
                const char *mnem, const char *_instMnem, uint64_t setFlags,
                InstRegIndex _src1, InstRegIndex _dest,
                uint8_t _srcSize, uint8_t _destSize, uint16_t _ext,
                OpClass __opClass) :
            X86MicroopBase(_machInst, mnem, _instMnem, setFlags, __opClass),
            src1(_src1.index()), dest(_dest.index()),
            srcSize(_srcSize), destSize(_destSize), ext(_ext)
        {}

        bool
        scalarOp() const
        {
            return ext & AVXScalarOp;
        }

        int
        numItems(int size) const
        {
            return scalarOp() ? 1 : (sizeof(uint64_t) / size);
        }

        bool
        multHi() const
        {
            return ext & AVXMultHiOp;
        }

        bool
        signedOp() const
        {
            return ext & AVXSignedOp;
        }

        bool xmmOp() const { return ext & AVXXMMOp; }

        bool ymmOp() const { return ext & AVXYMMOp; }

        bool zmmOp() const { return ext & AVXZMMOp; }
    };

    class AVXOpReg : public AVXOpBase
    {
      protected:
        const RegIndex src2;
        const RegIndex src3;

        // Constructor
        AVXOpReg(ExtMachInst _machInst,
                const char *mnem, const char *_instMnem, uint64_t setFlags,
                InstRegIndex _src1, InstRegIndex _src2, InstRegIndex _src3,
				InstRegIndex _dest,
                uint8_t _srcSize, uint8_t _destSize, uint16_t _ext,
                OpClass __opClass) :
            AVXOpBase(_machInst, mnem, _instMnem, setFlags,
                    _src1, _dest, _srcSize, _destSize, _ext, __opClass),
            src2(_src2.index()),
            src3(_src3.index())
        {}

        std::string generateDisassembly(Addr pc,
            const Loader::SymbolTable *symtab) const override;
    };

    class AVXOpImm : public AVXOpBase
    {
      protected:
        const RegIndex src2;
        uint8_t imm8;

        // Constructor
        AVXOpImm(ExtMachInst _machInst,
                const char *mnem, const char *_instMnem, uint64_t setFlags,
                InstRegIndex _src1, InstRegIndex _src2,
				uint8_t _imm8, InstRegIndex _dest,
                uint8_t _srcSize, uint8_t _destSize, uint16_t _ext,
                OpClass __opClass) :
            AVXOpBase(_machInst, mnem, _instMnem, setFlags,
                    _src1, _dest, _srcSize, _destSize, _ext, __opClass),
            src2(_src2.index()),
            imm8(_imm8)
        {}

        std::string generateDisassembly(Addr pc,
            const Loader::SymbolTable *symtab) const override;
    };
}

#endif //__ARCH_X86_INSTS_MICROAVXOP_HH__
