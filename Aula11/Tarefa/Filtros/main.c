#include <stdio.h>
#include <fcntl.h>
#include <io.h>

#define QTSAMPLES 160



int main() {
  FILE * in_file, * out_file;
  int i, n, n_amost;

  short entrada, saida;
  short sample[QTSAMPLES] = {
    0x0
  };

  float y = 0;

  //Carregando os coeficientes do filtro
  float coef[QTSAMPLES] = {
        #include "coeficientesPA.dat"
  };

  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("Sweep10_3600.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("saidaFiltro.pcm", "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  // zera vetor de amostras
  for (i = 0; i < QTSAMPLES; i++) {
    sample[i] = 0;
  }

  // execu��o do filtro
  do {

    //zera sa�da do filtro
    y = 0;

    //l� dado do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;

    //Convolu��o e acumula��o
    for (n = 0; n < QTSAMPLES; n++) {
      y += coef[n] * sample[n];
    }

    //desloca amostra
    for (n = QTSAMPLES - 1; n > 0; n--) {
      sample[n] = sample[n - 1];
    }

    saida = (short) y;

    //escreve no arquivo de sa�da
    fwrite( & saida, sizeof(short), 1, out_file);

  } while (n_amost);

  //fecha os arquivos de entrada de sa�da
  fclose(out_file);
  fclose(in_file);
  return 0;
}
