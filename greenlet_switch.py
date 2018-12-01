blueprint = manager.create_api_blueprint(Person, methods=['GET',
                                                          'POST'])
app.register_blueprint(blueprint)
