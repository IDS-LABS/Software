
#include <stdio.h>
#include <stddef.h>
#include <stdarg.h>
#include <errno.h>
#include <sys/types.h>   /* XXX for ssize_t on some platforms */

#ifdef _WIN32
#  include <Windows.h>
#  define snprintf _snprintf
typedef __int8 int8_t;
typedef __int16 int16_t;
typedef __int32 int32_t;
typedef __int64 int64_t;
typedef unsigned __int8 uint8_t;
typedef unsigned __int16 uint16_t;
typedef unsigned __int32 uint32_t;
typedef unsigned __int64 uint64_t;
typedef SSIZE_T ssize_t;
typedef unsigned char _Bool;
#else
#  include <stdint.h>
#endif


#include <sys/types.h>
#include <linux/i2c-dev.h>

int32_t _cffi_f_i2c_smbus_access(int x0, char x1, unsigned char x2, int x3, union i2c_smbus_data * x4)
{
  return i2c_smbus_access(x0, x1, x2, x3, x4);
}

int32_t _cffi_f_i2c_smbus_process_call(int x0, unsigned char x1, unsigned short x2)
{
  return i2c_smbus_process_call(x0, x1, x2);
}

int32_t _cffi_f_i2c_smbus_read_byte(int x0)
{
  return i2c_smbus_read_byte(x0);
}

int32_t _cffi_f_i2c_smbus_read_byte_data(int x0, unsigned char x1)
{
  return i2c_smbus_read_byte_data(x0, x1);
}

int32_t _cffi_f_i2c_smbus_read_word_data(int x0, unsigned char x1)
{
  return i2c_smbus_read_word_data(x0, x1);
}

int32_t _cffi_f_i2c_smbus_write_byte(int x0, unsigned char x1)
{
  return i2c_smbus_write_byte(x0, x1);
}

int32_t _cffi_f_i2c_smbus_write_byte_data(int x0, unsigned char x1, unsigned char x2)
{
  return i2c_smbus_write_byte_data(x0, x1, x2);
}

int32_t _cffi_f_i2c_smbus_write_quick(int x0, unsigned char x1)
{
  return i2c_smbus_write_quick(x0, x1);
}

int32_t _cffi_f_i2c_smbus_write_word_data(int x0, unsigned char x1, unsigned short x2)
{
  return i2c_smbus_write_word_data(x0, x1, x2);
}

int _cffi_const_I2C_PEC(long long *out_value)
{
  *out_value = (long long)(I2C_PEC);
  return (I2C_PEC) <= 0;
}

int _cffi_const_I2C_SLAVE(long long *out_value)
{
  *out_value = (long long)(I2C_SLAVE);
  return (I2C_SLAVE) <= 0;
}

int _cffi_const_I2C_SMBUS_BLOCK_DATA(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_BLOCK_DATA);
  return (I2C_SMBUS_BLOCK_DATA) <= 0;
}

int _cffi_const_I2C_SMBUS_BLOCK_MAX(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_BLOCK_MAX);
  return (I2C_SMBUS_BLOCK_MAX) <= 0;
}

int _cffi_const_I2C_SMBUS_BLOCK_PROC_CALL(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_BLOCK_PROC_CALL);
  return (I2C_SMBUS_BLOCK_PROC_CALL) <= 0;
}

int _cffi_const_I2C_SMBUS_BYTE(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_BYTE);
  return (I2C_SMBUS_BYTE) <= 0;
}

int _cffi_const_I2C_SMBUS_BYTE_DATA(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_BYTE_DATA);
  return (I2C_SMBUS_BYTE_DATA) <= 0;
}

int _cffi_const_I2C_SMBUS_I2C_BLOCK_BROKEN(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_I2C_BLOCK_BROKEN);
  return (I2C_SMBUS_I2C_BLOCK_BROKEN) <= 0;
}

int _cffi_const_I2C_SMBUS_I2C_BLOCK_DATA(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_I2C_BLOCK_DATA);
  return (I2C_SMBUS_I2C_BLOCK_DATA) <= 0;
}

int _cffi_const_I2C_SMBUS_PROC_CALL(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_PROC_CALL);
  return (I2C_SMBUS_PROC_CALL) <= 0;
}

int _cffi_const_I2C_SMBUS_QUICK(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_QUICK);
  return (I2C_SMBUS_QUICK) <= 0;
}

int _cffi_const_I2C_SMBUS_READ(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_READ);
  return (I2C_SMBUS_READ) <= 0;
}

int _cffi_const_I2C_SMBUS_WORD_DATA(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_WORD_DATA);
  return (I2C_SMBUS_WORD_DATA) <= 0;
}

int _cffi_const_I2C_SMBUS_WRITE(long long *out_value)
{
  *out_value = (long long)(I2C_SMBUS_WRITE);
  return (I2C_SMBUS_WRITE) <= 0;
}

static void _cffi_check_union_i2c_smbus_data(union i2c_smbus_data *p)
{
  /* only to generate compile-time warnings or errors */
  (void)((p->byte) << 1);
  (void)((p->word) << 1);
  { unsigned char(*tmp)[34] = &p->block; (void)tmp; }
}
ssize_t _cffi_layout_union_i2c_smbus_data(ssize_t i)
{
  struct _cffi_aligncheck { char x; union i2c_smbus_data y; };
  static ssize_t nums[] = {
    sizeof(union i2c_smbus_data),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(union i2c_smbus_data, byte),
    sizeof(((union i2c_smbus_data *)0)->byte),
    offsetof(union i2c_smbus_data, word),
    sizeof(((union i2c_smbus_data *)0)->word),
    offsetof(union i2c_smbus_data, block),
    sizeof(((union i2c_smbus_data *)0)->block),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_union_i2c_smbus_data(0);
}

