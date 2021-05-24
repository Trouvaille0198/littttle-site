<template>
  <div class="home pa-6">
    <v-text-field
      v-model="newTodoTitle"
      @click:append="addTodo"
      @keyup.enter="addTodo"
      class="pa-3"
      outlined
      label="Add todo"
      append-icon="mdi-plus"
      hide-details
      clearable
    ></v-text-field>
    <v-list flat class="pt-0">
      <v-list-item-group>
        <div v-for="todo in $store.state.todo.todos" :key="todo.id">
          <v-list-item
            @click="shiftTodo(todo.id)"
            :class="{ 'pink lighten-5': todo.is_done }"
          >
            <v-list-item-action>
              <v-checkbox :input-value="todo.is_done"></v-checkbox>
            </v-list-item-action>

            <v-list-item-content>
              <v-list-item-title
                :class="{
                  'text-decoration-line-through pink--text text--accent-4':
                    todo.is_done,
                }"
                >{{ todo.content }}</v-list-item-title
              >
            </v-list-item-content>
            <v-list-item-action>
              <v-btn icon @click.stop="deleteTodo(todo.id)">
                <v-icon color="primary lighten-1">mdi-delete</v-icon>
              </v-btn>
            </v-list-item-action>
          </v-list-item>
          <v-divider></v-divider>
        </div>
      </v-list-item-group>
    </v-list>
  </div>
</template>
<script>
export default {
  name: "Todo",
  data() {
    return {
      newTodoTitle: "",
    };
  },
  mounted: function () {
    this.$store.dispatch("readTodos");
  },
  methods: {
    addTodo() {
      if (this.newTodoTitle) {
        let newTodo = {
          id: Date.now(),
          content: this.newTodoTitle,
          created_time: Date.now(),
          is_done: false,
        };
        this.$store.dispatch("addTodo", newTodo);
        this.newTodoTitle = "";
      }
    },
    deleteTodo(id) {
      this.$store.dispatch("deleteTodo", id);
    },
    shiftTodo(id) {
      this.$store.dispatch("shiftTodo", id);
    },
  },
};
</script> 
