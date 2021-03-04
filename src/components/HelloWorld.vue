<template>
  <v-container>
    <v-row class="text-center" justify="center">
      <v-col cols="6">
        <div class="text-h4">Proto FASTAPI</div>
        <v-spacer></v-spacer>
        <v-btn block @click="printOutput('users')">
          Fetch Users
        </v-btn>
        <v-btn block @click="printOutput('posts')">
          Fetch Posts
        </v-btn>
        <v-btn block @click="printOutput('monsters')">
          Fetch Monsters
        </v-btn>
        <v-btn block @click="printOutput('weapons')">
          Fetch Weapons
        </v-btn>
      </v-col>
      <v-col cols="12">
        <div>{{ datas }}</div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex"
import { api } from "@/api.js"

export default {
  name: "HelloWorld",

  data() {
    return {
      datas: [],
    }
  },
  computed: {
    ...mapGetters(["getPort"]),
    ULR_API() {
      return `http://localhost:${this.getPort}/api/`
    },
  },
  methods: {
    async printOutput(queryType) {
      console.log(queryType)
      switch (queryType) {
        case "users":
          this.datas = await api.queryUsers()
          break
        case "posts":
          this.datas = await api.queryPosts()
          break
        case "monsters":
          this.datas = await api.queryMonsters()
          break
        case "weapons":
          this.datas = await api.queryWeapons()
          break

        default:
          break
      }
    },
  },
}
</script>

<style scoped>
button.v-btn {
  margin: 1rem 0 !important;
}
</style>
