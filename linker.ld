/* Memory */
MEMORY
{
  FLASH (rx)  : ORIGIN = 0x08000000, LENGTH = 128K
  RAM (rwx)   : ORIGIN = 0x20000000, LENGTH = 20K
}

/* Entry point */
ENTRY(Reset_Handler)

/* Symbols */
PROVIDE(_stack_start = ORIGIN(RAM) + LENGTH(RAM));
PROVIDE(_stack_end = ORIGIN(RAM));
PROVIDE(_heap_start = _edata);
PROVIDE(_heap_end = _stack_end);

/* Sections */
SECTIONS
{
  .isr_vector :
  {
    KEEP(*(.isr_vector))
  } > FLASH

  .text :
  {
    *(.text*)
    *(.rodata*)
    KEEP(*(.init))
    KEEP(*(.fini))
  } > FLASH

  /* Initialized data in RAM, loaded from FLASH */
  .data : AT (ADDR(.text) + SIZEOF(.text))
  {
    _sdata = .;
    *(.data*)
    _edata = .;
  } > RAM

  /* Uninitialized data */
  .bss :
  {
    __bss_start__ = .;
    *(.bss*)
    *(COMMON)
    __bss_end__ = .;
  } > RAM

  /* End of used RAM */
  _end = .;
}
