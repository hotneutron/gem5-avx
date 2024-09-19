#include "arch/x86/decoder.hh"

#include "arch/x86/regs/misc.hh"
#include "base/logging.hh"
#include "base/trace.hh"
#include "base/types.hh"
#include "debug/Decoder.hh"

namespace X86ISA {

enum EVEXTupleType {
  NOT_IMPLEMENTED = 0,
  O = NOT_IMPLEMENTED,
  FU,	// FULL
  FM,	// FULL_MEM
  FX,   // FU or FM
  HA,	// HALF
  T1,	// TUPLE1_SCALAR
  TF,	// TUPLE1_FIXED
  TX,	// TUPLE1_4X
  T2,	// TUPLE2
  T4,	// TUPLE4
  T8,	// TUPLE8
  HM,	// HALF_MEM
  QM,	// QUARTER_MEM
  EM,	// EIGHTH_MEM
  MX,	// MEM128
  MD	// MOVDDUP
};

const Decoder::ByteTable Decoder::EVEXTupleTypeTable[10] =
{
	{},
	// 0x00   0x0F
    {    //LSB
// MSB   O | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F
/*  O */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  1 */ FM, FM, T2, T2, FU, FU, T2, T2, O , O , O , O , O , O , O , O ,
/*  2 */ O , O , O , O , O , O , O , O , FM, FM, O , FM, O , O , T1, T1,
/*  3 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  4 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  5 */ O , FU, O , O , FU, FU, FU, FU, FU, FU, HA, FU, FU, FU, FU, FU,
/*  6 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  7 */ O , O , O , O , O , O , O , O , FU, FU, FU, O , O , O , O , O ,
/*  8 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  9 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  A */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  B */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  C */ O , O , FU, O , O , O , FU, O , O , O , O , O , O , O , O , O ,
/*  D */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  E */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  F */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O
	},
	// 0x66  0x0F
    {    //LSB
// MSB   O | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F
/*  O */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  1 */ FM, FM, T1, T1, FU, FU, T1, T1, O , O , O , O , O , O , O , O ,
/*  2 */ O , O , O , O , O , O , O , O , FM, FM, O , FM, O , O , T1, T1,
/*  3 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  4 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  5 */ FU, O , O , O , FU, FU, FU, FU, FU, FU, FU, FU, FU, FU, FU, FU,
/*  6 */ FM, FM, FU, FM, FM, FM, FU, FM, FM, FM, FU, FU, FU, FU, T1, FM,
/*  7 */ FU, FM, FU, FX, FM, FM, FU, O , HA, HA, HA, HA, O , O , T1, FM,
/*  8 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  9 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  A */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  B */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  C */ O , O , FU, O , T1, O , FU, O , O , O , O , O , O , O , O , O ,
/*  D */ O , MX, MX, MX, FU, FM, T1, O , FM, O , FM, FU, FM, FM, FM, FU,
/*  E */ FM, MX, MX, FM, FM, FM, FU, FM, FM, FM, FM, FU, FM, FM, FM, FU,
/*  F */ O , MX, MX, MX, FU, FM, FM, O , FM, FM, FU, FU, FM, FM, FU, O
	},
	// 0x66  0x0F38
    {    //LSB
// MSB   O | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F
/*  O */ FM, O , O , O , FM, O , O , O , O , O , O , FM, FU, FU, O , O ,
/*  1 */ FM, FM, FM, HM, FU, FU, FU, O , T1, T2, T4, T8, FM, FM, FU, FU,
/*  2 */ HM, QM, EM, HM, QM, HM, FM, FU, FU, FU, FM, FU, FU, T1, O , O ,
/*  3 */ HM, QM, EM, HM, QM, HM, FU, FU, FM, FU, FM, FU, FM, FU, FM, FU,
/*  4 */ FU, O , FU, T1, FU, FU, FU, FU, O , O , O , O , FU, T1, FU, T1,
/*  5 */ FU, FU, FU, FU, FM, FU, O , O , T1, T2, T4, T8, O , O , O , O ,
/*  6 */ O , O , T1, T1, FU, FU, FM, O , O , O , O , O , O , O , O , O ,
/*  7 */ FM, FU, FM, FU, O , FM, FU, FU, T1, T1, T1, T1, T1, FM, FU, FU,
/*  8 */ O , O , O , FU, O , O , O , O , T1, T1, T1, T1, O , FM, O , FM,
/*  9 */ T1, T1, T1, T1, O , O , FU, FU, FU, T1, FU, T1, FU, T1, FU, T1,
/*  A */ T1, T1, T1, T1, O , O , FU, FU, FU, T1, FU, T1, FU, T1, FU, T1,
/*  B */ O , O , O , O , FU, FU, FU, FU, FU, T1, FU, T1, FU, T1, FU, T1,
/*  C */ O , O , O , O , FU, O , T1, T1, FU, O , FU, T1, FU, T1, O , FM,
/*  D */ O , O , O , O , O , O , O , O , O , O , O , O , FM, FM, FM, FM,
/*  E */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  F */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O
	},
	// 0x66  0x0F3A
    {    //LSB
// MSB   O | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F
/*  O */ FU, FU, O , FU, FU, FU, O , O , FU, FU, T1, T1, O , O , O , FM,
/*  1 */ O , O , O , O , T1, T1, T1, T1, T4, T4, T8, T8, O , HM, FU, FU,
/*  2 */ T1, T1, T1, FU, O , FU, FU, T1, O , O , O , O , O , O , O , O ,
/*  3 */ O , O , O , O , O , O , O , O , T4, T4, T8, T8, O , O , FM, FM,
/*  4 */ O , O , FM, FU, FM, O , O , O , O , O , O , O , O , O , O , O ,
/*  5 */ FU, T1, O , O , FU, T1, FU, T1, O , O , O , O , O , O , O , O ,
/*  6 */ O , O , O , O , O , O , FU, T1, O , O , O , O , O , O , O , O ,
/*  7 */ FM, FU, FM, FU, O , O , O , O , O , O , O , O , O , O , O , O ,
/*  8 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  9 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  A */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  B */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  C */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , FU, FU,
/*  D */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  E */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  F */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O
	},
	// 0xF3  0x0F
    {    //LSB
// MSB   O | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F
/*  O */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  1 */ T1, T1, FM, O , O , O , FM, O , O , O , O , O , O , O , O , O ,
/*  2 */ O , O , O , O , O , O , O , O , O , O , T1, O , TF, TF, O , O ,
/*  3 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  4 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  5 */ O , T1, O , O , O , O , O , O , T1, T1, T1, FU, T1, T1, T1, T1,
/*  6 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , FM,
/*  7 */ FM, O , O , O , O , O , O , O , TF, TF, HA, T1, O , O , T1, FM,
/*  8 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  9 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  A */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  B */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  C */ O , O , T1, O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  D */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  E */ O , O , O , O , O , O , HA, O , O , O , O , O , O , O , O , O ,
/*  F */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O
	},
	// 0xF3  0x0F38
    {    //LSB
// MSB   O | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F
/*  O */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  1 */ HM, QM, EM, HM, QM, HM, O , O , O , O , O , O , O , O , O , O ,
/*  2 */ HM, QM, EM, HM, QM, HM, FM, FU, O , O , O , O , O , O , O , O ,
/*  3 */ HM, QM, EM, HM, QM, HM, O , O , O , O , O , O , O , O , O , O ,
/*  4 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  5 */ O , O , FU, O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  6 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  7 */ O , O , FU, O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  8 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  9 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  A */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  B */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  C */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  D */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  E */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  F */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O
	},
	{},
	// 0xF2
    {    //LSB
// MSB   O | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F
/*  O */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  1 */ T1, T1, MD, O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  2 */ O , O , O , O , O , O , O , O , O , O , T1, O , TF, TF, O , O ,
/*  3 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  4 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  5 */ T1, TX, TX, O , O , O , O , O , T1, T1, T1, O , T1, T1, T1, T1,
/*  6 */ O , O , O , O , O , O , O , O , FU, O , O , O , O , O , O , O ,
/*  7 */ FM, O , FU, O , O , O , O , O , TF, TF, FU, T1, O , O , O , O ,
/*  8 */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  9 */ O , O , O , O , O , O , O , O , O , O , TX, TX, O , O , O , O ,
/*  A */ O , O , O , O , O , O , O , O , O , O , TX, TX, O , O , O , O ,
/*  B */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  C */ O , O , T1, O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  D */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O ,
/*  E */ O , O , O , O , O , O , FU, O , O , O , O , O , O , O , O , O ,
/*  F */ O , O , O , O , O , O , O , O , O , O , O , O , O , O , O , O
	},
	{}
};

void Decoder::processCompressedDisplacement() {
	//emi.legacy.decodeVal   emi.evex.mm
	// 0x00(0)               0x0F(1)      :  1
	// 0x66(1)               0x0F(1)      :  2 
	// 0x66(1)               0x0F38(2)    :  3
	// 0x66(1)               0x0F3A(3)    :  4
	// 0xF3(4)               0xF0(1)      :  5
	// 0xF3(4)               0x0F38(2)    :  6
	// 0xF2(8)                            :  8
	uint8_t tableindex = emi.legacy.decodeVal +
				((emi.legacy.decodeVal != 8) ? (emi.evex.mm) : ( 0 ));
	ByteTable& dispNTable = EVEXTupleTypeTable[tableindex];
	int tupleType = dispNTable[emi.opcode.op];
	int shiftBits = 0;
	switch(tupleType) {
	case FU:
	case FX:
		shiftBits = (emi.evex.b) ? (emi.evex.w + 2) : (emi.evex.ll + 4);
		break;
	case HA:
		shiftBits = emi.evex.w + (emi.evex.b) ? (2) : (emi.evex.ll + 3);
		break;
	case FM:
		shiftBits = emi.evex.ll + 4;
		break;
	case T1:
		shiftBits = emi.evex.w + 2;
		//input size 8/16 bit??? how to distinguish??
		break;
	case TF:
		shiftBits = 3; // 64bits, 2: 32 bits???
		break;
	case TX:
		shiftBits = 4;
		break;
	case T2:	// Tuple2 W0, Tuple1 W1
		shiftBits = 3;
		break;
	case T4:	// Tuple4 W0, Tuple2 W1
		shiftBits = 4;
		break;
	case T8:	// Tuple8 W0, Tuple4 W1
		shiftBits = 5;
		break;
	case HM:
		shiftBits = emi.evex.ll + emi.evex.w + 3;
		break;
	case QM:
		shiftBits = emi.evex.ll + emi.evex.w + 2;
		break;
	case EM:
		shiftBits = emi.evex.ll + emi.evex.w + 1;
		break;
	case MX:
		shiftBits = 4;
		break;
	case MD:
		shiftBits = ( emi.evex.ll == 0 ) ? (3) : ( emi.evex.ll + 4 );
		break;
	}
	emi.displacement = emi.displacement << shiftBits;
//	uint8_t decodeVal = emi.legacy.decodeVal;
//	uint8_t mm = emi.evex.mm;
//	if( emi.opcode.op == 0x1a )
//		printf("tableindex: %d decodeVal: %d mm: %d tupleType: %x shiftBits: %d\n",
//				tableindex, decodeVal, mm, tupleType, shiftBits);
}

} // namespace X86ISA
