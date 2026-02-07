from __future__ import annotations

from datetime import date
from io import BytesIO

from flask import Flask, redirect, render_template, send_file, session, url_for
from flask_wtf import FlaskForm
from wtforms import DateField, SelectMultipleField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


TEST_OPTIONS = [
    ("avaliacao_neuropsicologica", "Avaliação neuropsicológica"),
    ("avaliacao_neurologica", "Avaliação neurológica"),
    ("avaliacao_comportamental", "Avaliação comportamental"),
    ("anamnese", "Anamnese"),
    ("entrevista_familiar", "Entrevista familiar"),
    ("observacao_clinica", "Observação clínica"),
    ("teste_padronizado", "Teste padronizado"),
    ("outros", "Outros"),
]


class SpecialistForm(FlaskForm):
    specialist_name = StringField("Nome do especialista", validators=[DataRequired()])
    specialty = StringField("Especialidade", validators=[DataRequired()])
    area = StringField("Área de atuação", validators=[DataRequired()])
    council_number = StringField("Número do conselho", validators=[Optional()])
    submit = SubmitField("Continuar para cadastro do paciente")


class PatientForm(FlaskForm):
    patient_name = StringField("Nome do paciente", validators=[DataRequired()])
    birth_date = DateField("Data de nascimento", validators=[DataRequired()])
    father_name = StringField("Nome do pai", validators=[Optional()])
    mother_name = StringField("Nome da mãe", validators=[Optional()])
    responsible = StringField("Responsáveis", validators=[Optional()])
    diagnosis = StringField("Diagnósticos do paciente", validators=[Optional()])
    purpose = StringField("Finalidade do documento", validators=[Optional()])
    cid_list = TextAreaField(
        "CID (lista com número e nome)",
        description="Ex: F84.0 - Transtorno do espectro autista",
        validators=[Optional()],
    )
    tests_done = SelectMultipleField(
        "Testes realizados (selecione quantos e quais)",
        choices=TEST_OPTIONS,
        validators=[Optional()],
    )
    exams_done = TextAreaField(
        "Quais são os exames feitos (inclua sugestões conforme o CID)",
        validators=[Optional()],
    )
    demand_description = TextAreaField(
        "Descrição da demanda",
        validators=[Optional()],
    )
    procedure_description = TextAreaField(
        "Procedimento (referencial teórico, recursos, duração)",
        validators=[Optional()],
    )
    analysis_overview = TextAreaField(
        "Análise (características principais e evolução)",
        validators=[Optional()],
    )
    method_exam = StringField("Cadastro de método - exame", validators=[Optional()])
    method_methodology = StringField("Cadastro de método - metodologia", validators=[Optional()])
    method_parameters = TextAreaField(
        "Cadastro de método - parâmetros adaptados ao paciente",
        validators=[Optional()],
    )
    reevaluation = TextAreaField(
        "Reavaliação (gráficos, resultados, interpretação)",
        validators=[Optional()],
    )
    performance_graphs = TextAreaField(
        "Gráficos de desempenho (numeração e legenda)",
        validators=[Optional()],
    )
    observations = TextAreaField(
        "Observações durante a intervenção",
        validators=[Optional()],
    )
    objectives_short = StringField("Objetivos de curto prazo", validators=[Optional()])
    objectives_medium = StringField("Objetivos de médio prazo", validators=[Optional()])
    objectives_long = StringField("Objetivos de longo prazo", validators=[Optional()])
    score_final = StringField("Score final com pontuação e evolução", validators=[Optional()])
    evolution = TextAreaField("Evolução", validators=[Optional()])
    conclusion_summary = TextAreaField("Conclusão - breve relato", validators=[Optional()])
    clinical_report = TextAreaField(
        "Relato clínico (hospitais por onde passou)",
        validators=[Optional()],
    )
    history = TextAreaField("Histórico", validators=[Optional()])
    positives = TextAreaField("Aspectos positivos", validators=[Optional()])
    difficulties = TextAreaField("Dificuldades apresentadas", validators=[Optional()])
    intervention_plan = TextAreaField("Plano de intervenção", validators=[Optional()])
    referrals = TextAreaField("Encaminhamentos", validators=[Optional()])
    closing = TextAreaField("Fecho", validators=[Optional()])
    submit = SubmitField("Gerar prévia")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

def calculate_age(birth_date: date) -> int:
    today = date.today()
    return today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )


def build_report_pdf(report_data: dict) -> BytesIO:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="SectionTitle", fontSize=12, leading=16, spaceAfter=8))
    styles.add(ParagraphStyle(name="BodyTextSmall", fontSize=10, leading=14))

    story = [
        Paragraph("INSTITUTO NADIA QUADROS", styles["Title"]),
        Paragraph(
            f"RELATÓRIO DE {report_data['specialist'].get('specialty', 'ESPECIALIDADE')}",
            styles["Heading2"],
        ),
        Spacer(1, 12),
    ]

    sections = report_data["sections"]
    for title, content in sections:
        story.append(Paragraph(title, styles["SectionTitle"]))
        story.append(Paragraph(content or "—", styles["BodyTextSmall"]))
        story.append(Spacer(1, 10))

    story.append(PageBreak())
    story.append(Paragraph("ENCERRAMENTO", styles["SectionTitle"]))
    story.append(
        Paragraph(
            report_data["closing"] or "Assinatura e carimbo do profissional.",
            styles["BodyTextSmall"],
        )
    )
    story.append(Spacer(1, 16))
    story.append(
        Paragraph(
            f"{report_data['specialist'].get('specialist_name', '')} — "
            f"{report_data['specialist'].get('specialty', '')} — "
            f"{report_data['specialist'].get('council_number', '')}",
            styles["BodyTextSmall"],
        )
    )

    doc.build(story)
    buffer.seek(0)
    return buffer


def build_sections(patient_data: dict, age: int, current_year: int) -> list[tuple[str, str]]:
    return [
        (
            "1. Identificação",
            (
                f"Nome: {patient_data['patient_name']}<br/>"
                f"Nascimento: {patient_data['birth_date']} (idade: {age})<br/>"
                f"Pai: {patient_data.get('father_name', '—')}<br/>"
                f"Mãe: {patient_data.get('mother_name', '—')}<br/>"
                f"Responsáveis: {patient_data.get('responsible', '—')}<br/>"
                f"Diagnósticos: {patient_data.get('diagnosis', '—')}<br/>"
                f"Finalidade ({current_year}): {patient_data.get('purpose', '—')}"
            ),
        ),
        ("CID", patient_data.get("cid_list", "—")),
        (
            "Testes realizados",
            ", ".join(patient_data.get("tests_done", [])) or "—",
        ),
        ("Exames feitos e sugestões", patient_data.get("exams_done", "—")),
        ("2. Descrição da demanda", patient_data.get("demand_description", "—")),
        ("3. Procedimento", patient_data.get("procedure_description", "—")),
        ("4. Análise", patient_data.get("analysis_overview", "—")),
        (
            "Cadastro de método",
            (
                f"Exame: {patient_data.get('method_exam', '—')}<br/>"
                f"Metodologia: {patient_data.get('method_methodology', '—')}<br/>"
                f"Parâmetros: {patient_data.get('method_parameters', '—')}"
            ),
        ),
        ("4.1 Reavaliação", patient_data.get("reevaluation", "—")),
        ("4.2 Gráficos de desempenho", patient_data.get("performance_graphs", "—")),
        ("4.3 Observações durante a intervenção", patient_data.get("observations", "—")),
        (
            "Objetivos",
            (
                f"Curto prazo: {patient_data.get('objectives_short', '—')}<br/>"
                f"Médio prazo: {patient_data.get('objectives_medium', '—')}<br/>"
                f"Longo prazo: {patient_data.get('objectives_long', '—')}"
            ),
        ),
        ("Score final e evolução", patient_data.get("score_final", "—")),
        ("Evolução", patient_data.get("evolution", "—")),
        ("5. Conclusão (breve relato)", patient_data.get("conclusion_summary", "—")),
        ("Relato clínico", patient_data.get("clinical_report", "—")),
        ("Histórico", patient_data.get("history", "—")),
        ("Aspectos positivos", patient_data.get("positives", "—")),
        ("Dificuldades apresentadas", patient_data.get("difficulties", "—")),
        ("Plano de intervenção", patient_data.get("intervention_plan", "—")),
        ("Encaminhamentos", patient_data.get("referrals", "—")),
    ]


@app.route("/", methods=["GET", "POST"])
def specialist():
    form = SpecialistForm()
    if form.validate_on_submit():
        session["specialist"] = {
            "specialist_name": form.specialist_name.data,
            "specialty": form.specialty.data,
            "area": form.area.data,
            "council_number": form.council_number.data,
        }
        return redirect(url_for("patient"))
    return render_template("specialist.html", form=form)


@app.route("/paciente", methods=["GET", "POST"])
def patient():
    if "specialist" not in session:
        return redirect(url_for("specialist"))
    form = PatientForm()
    current_year = date.today().year
    if not form.purpose.data:
        form.purpose.data = f"Relatório anual {current_year}"
    if form.validate_on_submit():
        session["patient"] = {
            "patient_name": form.patient_name.data,
            "birth_date": form.birth_date.data.isoformat(),
            "father_name": form.father_name.data,
            "mother_name": form.mother_name.data,
            "responsible": form.responsible.data,
            "diagnosis": form.diagnosis.data,
            "purpose": form.purpose.data,
            "cid_list": form.cid_list.data,
            "tests_done": form.tests_done.data,
            "exams_done": form.exams_done.data,
            "demand_description": form.demand_description.data,
            "procedure_description": form.procedure_description.data,
            "analysis_overview": form.analysis_overview.data,
            "method_exam": form.method_exam.data,
            "method_methodology": form.method_methodology.data,
            "method_parameters": form.method_parameters.data,
            "reevaluation": form.reevaluation.data,
            "performance_graphs": form.performance_graphs.data,
            "observations": form.observations.data,
            "objectives_short": form.objectives_short.data,
            "objectives_medium": form.objectives_medium.data,
            "objectives_long": form.objectives_long.data,
            "score_final": form.score_final.data,
            "evolution": form.evolution.data,
            "conclusion_summary": form.conclusion_summary.data,
            "clinical_report": form.clinical_report.data,
            "history": form.history.data,
            "positives": form.positives.data,
            "difficulties": form.difficulties.data,
            "intervention_plan": form.intervention_plan.data,
            "referrals": form.referrals.data,
            "closing": form.closing.data,
        }
        return redirect(url_for("preview"))
    return render_template("patient.html", form=form, current_year=current_year)


@app.route("/preview")
def preview():
    if "specialist" not in session or "patient" not in session:
        return redirect(url_for("specialist"))
    patient_data = session["patient"]
    birth_date = date.fromisoformat(patient_data["birth_date"])
    age = calculate_age(birth_date)
    current_year = date.today().year
    sections = build_sections(patient_data, age, current_year)
    return render_template(
        "preview.html",
        specialist=session["specialist"],
        patient=patient_data,
        age=age,
        sections=sections,
    )


@app.route("/pdf")
def pdf():
    if "specialist" not in session or "patient" not in session:
        return redirect(url_for("specialist"))
    patient_data = session["patient"]
    birth_date = date.fromisoformat(patient_data["birth_date"])
    age = calculate_age(birth_date)
    current_year = date.today().year
    report_data = {
        "specialist": session["specialist"],
        "sections": build_sections(patient_data, age, current_year),
        "closing": patient_data.get("closing", ""),
    }
    pdf_buffer = build_report_pdf(report_data)
    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="relatorio.pdf",
    )


@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("specialist"))


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5001)
