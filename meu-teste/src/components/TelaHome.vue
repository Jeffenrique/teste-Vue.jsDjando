<template>
  <div>
    <nav class="bar-nav">
      <div class="nav-wrapper">
        <a href="#" class="brand-logo">
          <img
            class="img-logo"
            src="https://i.ibb.co/Fh1PGQj/Logo-Preto-e-Laranja-de-Escola-do-Ensino-M-dio.png"
            alt=""
        /></a>

        <a href="#" data-activates="menu-mobile" class="button-collapse">
          <i class="material-icons">menu</i>
        </a>
        <ul class="right hide-on-med-and-down">
          <li><a v-on:click="TelaInicio">Início</a></li>
          <li><a v-on:click="TelaDisciplina">Disciplina</a></li>
          <li><a v-on:click="TelaCadastro">Cadastrar</a></li>
        </ul>
        <ul class="side-nav" id="menu-mobile">
          <li><a v-on:click="TelaInicio">Início</a></li>
          <li><a v-on:click="TelaDisciplina">Disciplina</a></li>
          <li><a v-on:click="TelaCadastro">Cadastrar</a></li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "tela-home",
};
</script>

<style scoped>
.bar-nav {
  background-color: #7f7fdc;
}
.img-logo {
  width: 97px;
  height: 60px;
  margin: 2px 0px 0px 14px;
}
.right {
  margin-right: 50px;
}
ul li a {
  color: black;
}
.button-collapse {
  color: black;
}
</style>