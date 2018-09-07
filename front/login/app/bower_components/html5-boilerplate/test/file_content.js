               }
                if ((ds.Tables["Curso"] != null)) {
                    base.Tables.Add(new CursoDataTable(ds.Tables["Curso"]));
                }
                if ((ds.Tables["Persona"] != null)) {
                    base.Tables.Add(new PersonaDataTable(ds.Tables["Persona"]));
                }
                if ((ds.Tables["Persona_Curso"] != null)) {
                    base.Tables.Add(new Persona_CursoDataTable(ds.Tables["Persona_Curso"]));
                }
                if ((ds.Tables["PromedioDeCursos"] != null)) {
                    base.Tables.Add(new PromedioDeCursosDataTable(ds.Tables["PromedioDeCursos"]));
                }
                this.DataSetName = ds.DataSetName;
                this.Prefix = ds.Prefix;
                this.Namespace = ds.Namespace;
                this.Locale = ds.Locale;
                this.CaseSensitive = ds.CaseSensitive;
                this.EnforceConstraints = ds.EnforceConstraints;
                this.Merge(ds, false, global::System.Data.MissingSchemaAction.Add);
                this.InitVars();
            }
            else {
                this.ReadXml(reader);
                this.InitVars();
            }
        }
        
        [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [global::System.CodeDom.Compiler.GeneratedCodeAttribute("System.Data.Design.TypedDataSetGenerator", "4.0.0.0")]
        protected override global::System.Xml.Schema.XmlSchema GetSchemaSerializable() {
            global::System.IO.MemoryStream stream = new global::System.IO.MemoryStream();
            this.WriteXmlSchema(new global::System.Xml.XmlTextWriter(stream, null));
            stream.Position = 0;
            return global::System.Xml.Schema.XmlSchema.Read(new global::System.Xml.XmlTextReader(stream), null);
        }
        
        [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [global::System.CodeDom.Compiler.GeneratedCodeAttribute("System.Data.Design.TypedDataSetGenerator", "4.0.0.0")]
        internal void InitVars() {
            this.InitVars(true);
        }
        
        [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [global::System.CodeDom.Compiler.GeneratedCodeAttribute("System.Data.Design.TypedDataSetGenerator", "4.0.0.0")]
        internal void InitVars(bool initTable) {
            this.tableCalificacion = ((CalificacionDataTable)(base.Tables["Calificacion"]));
            if ((initTable == true)) {
                if (