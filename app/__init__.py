from flask_migrate import Migrate
from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# Inicialización de las extensiones
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la aplicación desde el archivo config.py
    app.config.from_object(Config)
    
    # Inicializar las extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    
    # Registrar los blueprints
    from app.lugar import bp as lugar_bp
    app.register_blueprint(lugar_bp, url_prefix='/lugares')

    from app.persona import bp as persona_bp
    app.register_blueprint(persona_bp, url_prefix='/personas')

    from app.producto import bp as producto_bp
    app.register_blueprint(producto_bp, url_prefix='/producto')

    from app.recurso import bp as recurso_bp
    app.register_blueprint(recurso_bp, url_prefix='/recurso')

    from app.inventario import bp as inventario_bp
    app.register_blueprint(inventario_bp, url_prefix='/inventario')

    from app.material import bp as material_bp
    app.register_blueprint(material_bp, url_prefix='/material')

    from app.bom import bp as bom_bp
    app.register_blueprint(bom_bp, url_prefix='/bom')

    from app.orden_compra import bp as orden_compra_bp
    app.register_blueprint(orden_compra_bp, url_prefix='/orden_compra')

    from app.orden_produccion import bp as orden_produccion_bp
    app.register_blueprint(orden_produccion_bp, url_prefix='/orden_produccion')

    from app.centro_trabajo import bp as centro_trabajo_bp
    app.register_blueprint(centro_trabajo_bp, url_prefix='/centro_trabajo')

    from app.carga_trabajo import bp as carga_trabajo_bp
    app.register_blueprint(carga_trabajo_bp, url_prefix='/carga_trabajo')

    from app.calendario_capacidad import bp as calendario_capacidad_bp
    app.register_blueprint(calendario_capacidad_bp, url_prefix='/calendario_capacidad')

    from app.calendario_produccion import bp as calendario_produccion_bp
    app.register_blueprint(calendario_produccion_bp, url_prefix='/calendario_produccion')

    @app.route('/')
    def home():
        return render_template('index.html')

    return app



