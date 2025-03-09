
df_university = pd.read_csv('university_student_dashboard_data.csv)

def university_dashboard():
    st.title("University Admissions & Satisfaction Dashboard")

    st.write("### Total Applications and Enrollments per Term")
    term_summary = df_university.groupby('term')[['applications', 'enrollments']].sum()
    st.bar_chart(term_summary)

    st.write("### Retention Rate Over Time")
    retention_trend = df_university.groupby('year')['retention_rate'].mean()
    st.line_chart(retention_trend)

    st.write("### Student Satisfaction Scores")
    satisfaction_trend = df_university.groupby('year')['satisfaction_score'].mean()
    st.line_chart(satisfaction_trend)

    st.write("### Enrollment Breakdown by Department")
    department_enrollment = df_university.groupby('department')['enrollments'].sum()
    st.bar_chart(department_enrollment)

    st.write("### Comparison Between Spring and Fall Terms")
    term_comparison = df_university.groupby('term')[['applications', 'enrollments']].mean()
    st.bar_chart(term_comparison)
