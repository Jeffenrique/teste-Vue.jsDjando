<template>
  <div>
    <tela-home />
    <div class="tableDisciplina">
      <table class="responsive-table">
        <thead>
          <tr>
            <th>Disciplina</th>
            <th>Nome do aluno</th>
            <th>Nota 1º Unidade</th>
            <th>Nota 2º Unidade</th>
            <th>Média</th>
            <th>Situação</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="user of users" v-bind:key="user">
            <td>{{ user.nameDisciplina }}</td>
            <td>{{ user.nameAluno }}</td>
            <td>{{ user.nota1 }}</td>
            <td>{{ user.nota2 }}</td>
            <td>{{ user.media }}</td>
            <td>{{ user.situacao }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TelaHome from "./TelaHome.vue";

export default {
  components: { TelaHome },
  name: "teste",
  data() {
    return {
      users: [],
    };
  },
  created: function () {
    
    axios
      .get(" http://127.0.0.1:8000/api/users")
      .then((result) => {
        this.users = result.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style>
.tableDisciplina {
  margin: 50px;
}
</style>
