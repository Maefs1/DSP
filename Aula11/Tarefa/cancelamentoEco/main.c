#include <stdio.h>
#include <fcntl.h>
#include <io.h>

#define NSAMPLES 160
#define MU 0.000000000005

int main() {
  FILE *far, *near,*out_file;
  int i, n, n_amost, n_amost_near;

  short entrada, saida, xn[NSAMPLES];

  double wn [NSAMPLES];
  double yn = 0.0;
  double erro = 0.0;


  /* abre os arquivos de entrada e saida */
  if ((far = fopen("far_apcm.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }

  if ((near = fopen("near_apcm.pcm", "rb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("saidaCancelamentoEco.pcm", "wb")) == NULL) {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }


  // zera vetor de amostras
  for (i = 0; i < NSAMPLES; i++) {
    xn[i] = 0;
    wn[i] = 0.0;
  }

  do {

    yn = 0;

    // l� far do arquivo
    n_amost = fread( & entrada, sizeof(short), 1, far);
    xn[0] = entrada;


    // convolu��o da sa�da do filtro y(n)
    for (n = 0; n < NSAMPLES; n++) {
      yn += wn[n] * xn[n];
    }

    // l� near do arquivo
    fread( & entrada, sizeof(short), 1, near);
    // erro = near - y(n)
    erro = entrada - yn;
    //printf("Erro: %f\n", erro);

    // atualizando os coeficientes do filtro usando lms
    for (n = 0; n < NSAMPLES; n++) {
        wn[n] = wn[n] + MU * erro * xn[n];
    }

    // atualizando o x(n)
    for (n = NSAMPLES - 1; n > 0; n--) {
      xn[n] = xn[n - 1];
    }

    saida = (short) erro;

    //escreve no arquivo de sa�da
    fwrite( & saida, sizeof(short), 1, out_file);

  } while (n_amost);

  //fecha os arquivos de entrada de sa�da
  fclose(out_file);
  fclose(far);
  fclose(near);
  return 0;
}
