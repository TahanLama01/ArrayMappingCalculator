# ArrayMappingCalculator
```
Program dibuat dari Matkul Struktur Data
Program akan menghitung Mapping Array Dimensi 1, 2, dan 3.
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------
```
                                                        Rumus Array Dimensi 1

Rumus : @A[i] = B + (i – 1) * L

Keterangan :
  @A[i] : Posisi Array yg dicari
  B : Posisi awal index di memory komputer
  i : Subkrip atau indeks array yg dicari
  L : Ukuran / Besar memory suatu type data
  
  Contoh :
A[3].....
          = 0011(H) + (3 - 1) * 2
          = 0011(H) + 4(D)
          = 0011(H) + 4(H)
          = 0015(H)
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------
```
                                                        Rumus Array Dimensi 2

Rumus1 : Secara Baris Per Baris (Row Major Order / RMO)
@M[i][j]  = M[0][0] + ((j - 1) * N + (i - 1)) * L

Rumus2 : Secara Kolom Per Kolom (Coloumn Major Order/CMO)
@M[i][j]  = M[0][0] + ((j - 1) * K + (i - 1)) * L

Keterangan :
  @M[i][j] = Posisi Array yg dicari
  M[0][0] = Posisi alamat awal index array,
  i = Baris
  j = kolom
  L = Ukuran memory type data
  K = Banyaknya elemen per kolom
  N = Banyaknya elemen per baris
  
  Contoh :
Rumus1 : Secara Baris Per Baris (Row Major Order / RMO)
@M[i][j]  = M[0][0] + ((j - 1) * N + (i - 1)) * L
A[3][2]..... Secara Baris Per Baris (Row Major Order / RMO)
          = 0011(H) + ((2 - 1) * 2 + (3 - 1)) * 2
          = 0011(H) + 8(D)
          = 0011(H) + 8(H)
          = 0019(H)


Rumus2 : Secara Kolom Per Kolom (Coloumn Major Order/CMO)
@M[i][j]  = M[0][0] + ((j - 1) * K + (i - 1)) * L
A[3][2]..... Secara Kolom Per Kolom (Coloumn Major Order/CMO)
          = 0011(H) + ((2 - 1) * 3 + (3 - 1)) * 2
          = 0011(H) + 10(D)
          = 0011(H) + A(H)
          = 0011(H)
```
-------------------------------------------------------------------------------------------------------------------------------------------------------------
```
                                                        Rumus Array Dimensi 3

@M[m][n][p]   = M[0][0][0] + (((m-1) *(jum.elemen2 *jum.elemen3)) + ((n-1)*(jum.elemen3)) + ((p-1))* L

Keterangan :
  @M[m][n][p] = Posisi Array yg dicari
  jum.elemen1 = Banyak/batas index Baris/Tinggi 
  jum.elemen2 = Banyak/batas index Kolom/Lebar 
  jum.elemen2 = Banyak/batas index Blok/Panjang 
  m = Lokasi index 1 
  n = Lokasi index 2 
  p = Lokasi index 3 
  L: Ukuran / Besar memory suatu type data 


  Contoh :
A[2][3][2].....
              = 0021(H) + (((2 - 1) * (3 * 4)) + ((3 - 1) * 4) + (2 - 1)) * 4
              = 0021(H) + (12 + 8 + 1) * 4
              = 0021(H) + 84(D)
              = 0021(H) + 54(H)
              = 0075(H
```
---------------------------------------------------------------------------------------------------------
           
